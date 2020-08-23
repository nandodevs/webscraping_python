import requests
import json
from bs4 import BeautifulSoup

res = requests.get('linkdosite')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(class_='poster')

all_posts = []
for post in posts:
    info = post.find(class_='poster')
    ano = info.find(class_='t-ano').text
    title = info.find(class_='t-tit').text
    time = info.find(class_='t-tempo').text
    audio = info.find(class_='t-audio').text
    img = info.find(class_='thumb')['data-src']

    all_posts.append(
        {'titulo': title,
         'ano': ano,
         'img': img,
         'tempo': time,
         'audio': audio
         })

print(all_posts)
with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)













