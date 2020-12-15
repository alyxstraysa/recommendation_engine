from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Anime_User

# Create your views here.

def index(request):
    #context={}
    return render(request, 'anime_app/index.html')

def user_rec(request, user_id, rank_id):
    # try:
    #     user = Anime_User.objects.get(pk=user_id)
    # except Anime_User.DoesNotExist:
    #     raise Http404('User ID does not exist')
    # return HttpResponse("You have just entered the %s recommendation for %s" % (rank_id, user_id))
    #user_id = get_object_or_404(Anime_User, pk=user_id)
    return render(request, 'anime_app/user_rec.html', {'user_id': user_id})