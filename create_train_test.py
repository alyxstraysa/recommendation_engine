import math
import random
import numpy as np

with open('fulltrain.txt', 'r') as file:
    for line in file.readlines():
        lineModified = line.replace("\n", " ").strip().split(" ")

        if len(lineModified) <= 10:
            print("No items found for user: {userid} or the number of items is too low!".format(userid=userid))
            continue
        else: 
            userid = lineModified[0]
            userid = int(userid)
            items = lineModified[1:]
            items = [int(x) for x in items]
            select_num = math.floor(len(items) * (2/3))
            train_items = sorted(random.sample(items, select_num))
            test_items = sorted(np.setdiff1d(items, train_items))

            userid = str(userid)
            train_items = [str(item) for item in train_items]
            test_items = [str(item) for item in test_items]

            train_items = " ".join(train_items)
            test_items = " ".join(test_items)

            with open("train.txt", "a+") as f:
                f.write(str(userid) + " " + str(train_items) + '\n')
            
            with open("test.txt", "a+") as f:
                f.write(str(userid) + " " + str(train_items) + '\n')