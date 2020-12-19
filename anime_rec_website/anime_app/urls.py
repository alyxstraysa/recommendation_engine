from django.urls import path
from . import views
import requests

ANIME_DICT = {}
USER_ANIMES = {}

def getRemappedAnime(user_animes):
    #Returns the list of remapped anime IDS
    output_list = []
    for anime_id in user_animes:
        try:
            output_list.append(anime_dict[str(anime_id)])
        except:
            pass
    
    return output_list
    
    
def setUp():
    with open("./LightGCN-PyTorch/data/anime/anime.txt") as f:
        next(f)
        for line in f.readlines():
                lineModified = line.split(" ")
                anime, animeID = lineModified[0].strip('\n'), lineModified[1].strip('\n')
                ANIME_DICT[animeID] = anime

    
    with open("./LightGCN-PyTorch/data/anime/train.txt") as f:
        next(f)
        for line in f.readlines():
            lineModified = line.split(" ")
            user, animes = lineModified[0].strip('\n'), [int(x.strip('\n')) for x in lineModified[1:]]
            USER_ANIMES[user] = animes

def getLevensteinDistance(user_animes):
    #(Count, User)
    maxSimilarity = (0, None)
    lastUserID = 0
    for user,animes in USER_ANIMES.items():
        count = 0
        for anime in user_animes:
            if int(anime) in animes:
                count += 1
        if count > maxSimilarity[0]:
            maxSimilarity = (count, user)
        lastUserID = user
    # for user, animes in USER_ANIMES.items():
    #     simCalc = lev.similarity(user_animes, animes)
    #     print(simCalc)
    #     if simCalc > maxSimilarity[0]:
    #         maxSimilarity = (simCalc, user)
    if maxSimilarity == (0, None):
        return lastUserID
    return maxSimilarity[1]

def testRequest(user):
    r = requests.get('https://api.jikan.moe/v3/user/{user}/animelist/all'.format(user=user.strip()))
    req_json = r.json()
    anime_list = []
    for anime in req_json['anime']:
        anime_list.append(anime['mal_id'])

    user_remap_animes = getRemappedAnime(anime_list)
    return user_remap_animes

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_rec, name='user_rec'),
    path('anime_view', views.anime_view, name='anime_view')
]

# if __name__ == '__main__':
#     test_animes = testRequest('exorchids')
#     setUp()
#     remap = getRemappedAnime(test_animes)
#     simUser = getLevensteinDistance(remap)
#     print(simUser)
