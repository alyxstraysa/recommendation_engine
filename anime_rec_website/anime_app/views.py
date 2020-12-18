from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Anime_User
from .mal_retriever import get_Anime_Info

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
    recommendations = [39617,39617,39617,39617,39617,39617,39617,39617,39617]
    for anime_ID in recommendations:
        anime_name, anime_image = get_Anime_Info(anime_ID)
        context['names'].append(anime_name)
        context['images'].append(anime_image)
    return render(request, 'anime_app/user_rec.html', context)