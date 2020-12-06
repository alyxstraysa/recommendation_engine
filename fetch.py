import requests

id_counter = 0

for user in user_list:
    r = requests.get('https://api.jikan.moe/v3/user/{user}/animelist/all'.format(user=user))
    anime_list = r.json()
    anime_list = anime_list['anime']

    with open("user.txt", "w") as f:
        f.write(user, id_counter)

    with open("filename.txt", "w") as f:
        for anime in anime_list:
            f.write((anime['mal_id'], anime['title'], anime['score']))

    
    id_counter += 1



#step 1 fetch all anime in dataset and ID and remap the ids into dictionary
#using a user, search all his anime then add keypairs
