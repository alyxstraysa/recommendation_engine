from django.db import models

# Create your models here.
class Anime_Pref(models.Model):
    anime_name = models.CharField('anime_name', max_length=200)

    def __str__(self):
        return self.anime_name

class Anime_User(models.Model):
    anime_pref = models.ManyToManyField(Anime_Pref)
    user_name = models.CharField('user_name', max_length= 50)

    def __str__(self):
        return self.user_name + ":  [" + self.anime_pref + "]"