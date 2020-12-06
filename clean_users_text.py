
def cleanFile(file_path):
    '''
    Cleans up user.txt file to remove duplicates
    :param file_path:
    :return: Void
    '''
    index = 0
    users = {}

    with open(file_path + "user.txt", "r") as file:
        for user in file.readlines():
            if user.strip("\n") not in users:
                users[user.strip("\n")] = index
                index += 1

    #Write to another file
    with open(file_path + '/mal_data/' + "user.txt" , "w") as file:
        file.write('org_id remap_id\n')
        for user_name, user_id in users.items():
            line_to_add = str(user_name) + str(user_id) + "\n"
            file.write(line_to_add)

if __name__ == '__main__':
    FILE_PATH =  './data/'
    cleanFile(FILE_PATH)



