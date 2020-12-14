from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('anime_app/index.html')
    context={}
    return HttpResponse(template.render(context, request))

def user_rec(request, user_id, rank_id):
    return HttpResponse("You have just entered the %s recommendation for %s" % (rank_id, user_id))