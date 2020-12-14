import requests
import time

DATA_FILE_PATH = './data/mal_data/'

if __name__ == "__main__":
    #read all users into a list called user list
    user_list = []

    id_counter = 0
    anime_id_counter = 0

    anime_dict = {}
    iterations = 0
    with open(DATA_FILE_PATH + 'user.txt', 'r') as file:
        next(file)
        for line in file.readlines():
            lineModified = line.split(" ")
            user, userID = lineModified[0].strip('\n'), lineModified[1].strip('\n')
            r = requests.get('https://api.jikan.moe/v3/user/{user}/animelist/all'.format(user=user.strip()))
            anime_json = r.json()
            try:
                'anime' in anime_json
                anime_info = anime_json['anime']
            except:
                continue
            for anime in anime_info:
                if anime['mal_id'] in anime_dict.keys():
                    pass
                else:
                    anime_dict[anime['mal_id']] = anime_id_counter
                    anime_id_counter += 1

            with open(DATA_FILE_PATH + "train.txt", "a") as f:
                anime_data = [str(userID)]

                for anime in anime_info:
                    #append the remapped anime to the list then join
                    anime_data.append(str(anime_dict[anime['mal_id']]))

                anime_write = " ".join(anime_data) + '\n'
                f.write(anime_write)

            iterations += 1
            if iterations == 100:
                break
            #delay of one second for rate limiter
            time.sleep(1.0)


    #Writing to anime.txt
    with open(DATA_FILE_PATH + "anime.txt", "a") as file:
        file.write("item_id, remap_id" + '\n')
        for malAnimeID, remapID in anime_dict.items():
            file.write(str(malAnimeID) + " " + str(remapID) + '\n')

    with open(DATA_FILE_PATH + "anime_mapping.txt", "a") as file:
        file.write("remap_id, item_id" + '\n')
        for malAnimeID, remapID in anime_dict.items():
            file.write(str(remapID) + " " + str(malAnimeID) + '\n')

