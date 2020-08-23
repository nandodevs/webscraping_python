import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.filmesonlinegratisbr.com/genero/lancamentos/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')


all_posts = soup.find_all(class_='box')

print(all_posts)