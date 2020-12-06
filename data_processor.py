import requests
import time

if __name__ == "__main__":
    #read all users into a list called user list
    user_list = []

    id_counter = 0
    anime_id_counter = 0

    anime_dict = {}

    for user in user_list:
        r = requests.get('https://api.jikan.moe/v3/user/{user}/animelist/all'.format(user=user))
        anime_json = r.json()
        anime_info = anime_json['anime']

        if len(anime_info) <= 10:
            break

        for anime in anime_info:
            if anime in anime_dict:
                pass
            else:
                anime_dict[anime['mal_id']] = anime_id_counter
        

        else:
            with open("/data/mal_data/user_list.txt", "a") as f:
                f.write(user + " " + str(id_counter) + '\n')
            
            with open("/data/mal_data/anime_list.txt", "a") as f:
                #need to iterate over all anime in anime
                anime_data = ['id_counter']

                for anime in anime_info:
                    #append the remapped anime to the list then join
                    anime_data.append(anime_dict[anime['mal_id']])

                anime_write = " ".join(anime_data)
                f.write(anime_write)
                

    #delay of one second for rate limiter
    time.sleep(1.5)