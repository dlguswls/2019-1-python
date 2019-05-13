from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup


r = requests.get(episode_url)
soup = BeautifulSoup(r.text, 'html.parser')

comic_title = ' '.join(soup.select('.list_area daily_img a[class*=img_list')
ep_title = ' '.join(soup.select('.title a[class*=nclk_v2')
comic_score = ' '.join(soup.select('.vote_lst a[class*=nclk_v2')

for comic,episode,score in zip(comic_title , ep_title, comic_score):
    c = ''.join(comic)
    e = ''.join(episode)
    s = ''.join(score)

print("{}/{}/{}",format(c,e,s))