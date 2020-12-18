'''
Created on Mar 1, 2020
Pytorch Implementation of LightGCN in
Xiangnan He et al. LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation
@author: Jianbai Ye (gusye@mail.ustc.edu.cn)

Design training and test process
'''
import world
import numpy as np
import torch
import utils
import dataloader
from pprint import pprint
from utils import timer
from time import time
from tqdm import tqdm
import model
import multiprocessing
from sklearn.metrics import roc_auc_score


CORES = multiprocessing.cpu_count() // 2


def BPR_train_original(dataset, recommend_model, loss_class, epoch, neg_k=1, w=None):
    Recmodel = recommend_model
    Recmodel.train()
    bpr: utils.BPRLoss = loss_class
    
    with timer(name="Sample"):
        #UniformSample_original => [[user, positive item they liked, negative item not associated with them], ...]
        S = utils.UniformSample_original(dataset)
    #[user1, positem1, negItem1]
    #[user2, positem2, negItem2]
    #All user, positive items, and negative item lists
    users = torch.Tensor(S[:, 0]).long()
    posItems = torch.Tensor(S[:, 1]).long()
    negItems = torch.Tensor(S[:, 2]).long()

    users = users.to(world.device)
    posItems = posItems.to(world.device)
    negItems = negItems.to(world.device)
    #Shuffling in batches
    users, posItems, negItems = utils.shuffle(users, posItems, negItems)
    total_batch = len(users) // world.config['bpr_batch_size'] + 1
    aver_loss = 0.
    for (batch_i,
         (batch_users,
          batch_pos,
          batch_neg)) in enumerate(utils.minibatch(users,
                                                   posItems,
                                                   negItems,
                                                   batch_size=world.config['bpr_batch_size'])):
        cri = bpr.stageOne(batch_users, batch_pos, batch_neg)
        aver_loss += cri
        if world.tensorboard:
            w.add_scalar(f'BPRLoss/BPR', cri, epoch * int(len(users) / world.config['bpr_batch_size']) + batch_i)
    aver_loss = aver_loss / total_batch
    time_info = timer.dict()
    timer.zero()
    return f"loss{aver_loss:.3f}-{time_info}"
    
    
def test_one_batch(X):
    sorted_items = X[0].numpy()
    groundTrue = X[1]
    r = utils.getLabel(groundTrue, sorted_items)
    pre, recall, ndcg = [], [], []
    for k in world.topks:
        ret = utils.RecallPrecision_ATk(groundTrue, r, k)
        pre.append(ret['precision'])
        recall.append(ret['recall'])
        ndcg.append(utils.NDCGatK_r(groundTrue,r,k))
    return {'recall':np.array(recall), 
            'precision':np.array(pre), 
            'ndcg':np.array(ndcg)}
        
            
def Infer(dataset, Recmodel, user):
    dataset: utils.BasicDataset
    testDict: dict = dataset.testDict
    Recmodel: model.LightGCN
    user: string = userid
    # eval mode with no dropout
    Recmodel = Recmodel.eval()
    max_K = max(world.topks)
    with torch.no_grad():
        users = list(testDict.keys())
        users_list = []
        rating_list = []
        groundTrue_list = []

        allPos = dataset.getUserPosItems([user])
        batch_users_gpu = torch.Tensor([user]).long()
        batch_users_gpu = batch_users_gpu.to(world.device)

        rating = Recmodel.getUsersRating(batch_users_gpu)
        #rating = rating.cpu()
        exclude_index = []
        exclude_items = []
        for range_i, items in enumerate(allPos):
            exclude_index.extend([range_i] * len(items))
            exclude_items.extend(items)
        rating[exclude_index, exclude_items] = -(1<<10)
        _, rating_K = torch.topk(rating, k=max_K)
        rating = rating.cpu().numpy()

        rating_K = rating_K.cpu().numpy()
        
        prediction = rating_K[0]

        anime_dict = {}

        with open("../data/anime/anime.txt") as f:
            next(f)

            for line in f.readlines():
                    lineModified = line.split(" ")
                    anime, animeID = lineModified[0].strip('\n'), lineModified[1].strip('\n')
                    anime_dict[animeID] = anime

        output_list = []

        for anime_id in prediction:
            try:
              output_list.append(anime_dict[str(anime_id)])
            except:
                pass

        ' '.join([str(elem) for elem in output_list])
        print(output_list)

        return rating