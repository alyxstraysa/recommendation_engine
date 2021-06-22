from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Anime_User
from .mal_retriever import get_Anime_Info
import time

def getRemappedAnime(user_animes):
    #Returns the list of remapped anime IDS
    output_list = []
    for anime_id in user_animes:
        try:
            output_list.append(anime_dict[str(anime_id)])
        except:
            pass
    
    return output_list
    
# Create your views here.

def index(request):
    #context={}
    return render(request, 'anime_app/index.html')

def anime_view(request):
    context = {'mal_un': request.POST.get('mal_username', ''),
               'user_id': None,
               'names': [],
               'images': [],
               'synopsis': []
               }

    recommendations = [39617,9919,1818,1575,2025,270,1604,339,10798]
    for anime_ID in recommendations:
        time.sleep(4)
        anime_name, anime_image, synopsis = get_Anime_Info(anime_ID)
        print(anime_name, anime_image)
        context['names'].append(anime_name)
        context['images'].append(anime_image)
        context['synopsis'].append(synopsis)

    print("Requesting information for {mal_un}".format(mal_un = context['mal_un']))
    return render(request, 'anime_app/user_rec.html', context)
