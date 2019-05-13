import requests
from bs4 import BeautifulSoup

r = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
soup = BeautifulSoup(r.text, 'html.parser')

comics = soup.select('.list_area daily_img > ul >li')
titlelist = []
linklist = []
scorelist = []
episodelist = []

for x in comics:
    title = x.find('a').get('title')
    for y in title:
        ep_title = y.select('.title a[class*=nclk_v2]')
        episodelist.append(ep_title)
    link = x.find('a').get('herf')
    score = x.find('.rating_type > span > strong')
    titlelist.append(title)
    linklist.append(link)
    scorelist.append(score)
print(titlelist,linklist,scorelist,episodelist)
