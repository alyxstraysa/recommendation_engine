from lxml import html
import requests
import time
import random

if __name__ == "__main__":
    for i in range(1000):
        link = 'https://myanimelist.net/users.php?lucky=1'
        page = requests.get(link)
        tree = html.fromstring(page.content)
        names = tree.xpath('//td[@align="center"]/div/a/text()')

        with open("data/user.txt", "a") as f:
            for name in names:
                f.write(name+ " " + '\n')

        time.sleep(random.randint(5, 10))