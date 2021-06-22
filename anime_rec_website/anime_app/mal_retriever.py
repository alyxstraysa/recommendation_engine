import requests
from bs4 import BeautifulSoup

def get_PictureURL(anime_ID):
    r = requests.get('https://api.jikan.moe/v3/anime/{}/pictures'.format(anime_ID))
    anime_json = r.json()
    if 'pictures' in anime_json:
        picture = anime_json['pictures'][0]
        if 'small' in picture:
            return picture['small']
        elif 'large' in picture:
            return picture['large']
        else:
            return 'N/A'
    else:
        return 'N/A'

def get_Anime_Info(anime_ID):
    url="https://api.jikan.moe/v3/anime/{anime_id}/".format(anime_id = anime_ID)

    r = requests.get(url)
    anime = r.json()
    print(anime)
    anime_name = anime['title']
    #mal_id = anime['mal_id']
    image_source = anime['image_url']

    #todo return summary

    return anime_name, image_source
