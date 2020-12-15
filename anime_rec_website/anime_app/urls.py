from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/<int:rank_id>/', views.user_rec, name='user_rec')
]