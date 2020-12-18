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
    url="https://myanimelist.net/anime/{}/".format(anime_ID)

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    #print(soup.prettify()) # print the parsed data of html
    anime_name = soup.title.text.replace("- MyAnimeList.net", "").strip()
    tags=soup.findAll('img', alt=True)
    image_source = None
    for tag in tags:
        if anime_name in tag['alt']:
            image_source = tag['data-src']
    return anime_name, image_source
# if __name__ == '__main__':
#     #print(get_PictureURL(40455))
#     anime_name, image_source = get_Anime_Info(39617)
#     print(anime_name, image_source)