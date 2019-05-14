import requests
from bs4 import BeautifulSoup

r = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
soup = BeautifulSoup(r.text, 'html.parser')

comics = soup.select('.list_area.daily_img > ul >li')
episodes = soup.select('.tit_area.view')
titlelist = []
linklist = []

i=0
for x in comics:
    title = x.find('a').get('title')
    link = x.find('a').get('href')
    titlelist.append(title)
    linklist.append(link)
    print(titlelist[i],linklist[i])
    i+=1