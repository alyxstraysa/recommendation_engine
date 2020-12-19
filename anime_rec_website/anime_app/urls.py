from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_rec, name='user_rec'),
    path('anime_view', views.anime_view, name='anime_view')
]