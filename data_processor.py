import requests
import time

DATA_FILE_PATH = './data/mal_data/'

if __name__ == "__main__":
    #read all users into a list called user list
    user_list = []
    anime_id_counter = 0

    anime_dict = {}

    with open(DATA_FILE_PATH + 'user.txt', 'r') as file:
        next(file)
        
        counter = 0

        for line in file.readlines():
            if counter == 5000:
                break

            lineModified = line.split(" ")
            user, userID = lineModified[0].strip('\n'), lineModified[1].strip('\n')
            print("Writing user: {user} with userID: {userID}".format(user=user, userID=userID))
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

            #delay of 4 seconds for rate limiter
            print("Finished writing!")
            time.sleep(4.0)
            counter += 1


    #Writing to anime.txt
    with open(DATA_FILE_PATH + "anime.txt", "a") as file:
        file.write("item_id, remap_id" + '\n')
        for malAnimeID, remapID in anime_dict.items():
            file.write(str(malAnimeID) + " " + str(remapID) + '\n')

