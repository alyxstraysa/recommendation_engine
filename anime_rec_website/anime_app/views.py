from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Anime_User
from .mal_retriever import get_Anime_Info

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

def user_rec(request, user_id):
    # try:
    #     user = Anime_User.objects.get(pk=user_id)
    # except Anime_User.DoesNotExist:
    #     raise Http404('User ID does not exist')
    # return HttpResponse("You have just entered the %s recommendation for %s" % (rank_id, user_id))
    #user_id = get_object_or_404(Anime_User, pk=user_id)
    context = {'user_id': user_id, 'names': [], 'images': []}
    r = requests.get('https://api.jikan.moe/v3/user/{user}/animelist/all'.format(user=user.strip()))
    req_json = r.json()
    anime_list = []
    for anime in req_json['anime']:
        anime_list.append(anime['mal_id'])

    user_remap_animes = getRemappedAnime(anime_list)
    
    

    recommendations = [39617,39617,39617,39617,39617,39617,39617,39617,39617]
    for anime_ID in recommendations:
        anime_name, anime_image = get_Anime_Info(anime_ID)
        context['names'].append('')
        context['images'].append(anime_image)
    return render(request, 'anime_app/user_rec.html', context)

def anime_view(request):
    context = {}
    print("Requesting information for {mal_un}".format(mal_un = request.POST.get('mal_username', '')))
    return render(request, 'anime_app/user_rec.html', context)