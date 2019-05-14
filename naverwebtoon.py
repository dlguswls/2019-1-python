import requests
from bs4 import BeautifulSoup

r = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
soup = BeautifulSoup(r.text, 'html.parser')

comics = soup.select('.list_area.daily_img > ul >li')
episodes = soup.select('tbody>tr')
titlelist = []
linklist = []
episodelist = []
epscorelist = []
epdaylist = []
i=0
k=0
for x in comics:
    title = x.find('a').get('title')
    link = x.find('a').get('href')
    titlelist.append(title)
    linklist.append(link)
    print(titlelist[i],linklist[i])
    i+=1
    for y in episodes:
        ep_title = y.find('a').get('nclk_v2')
        ep_score = y.find('strong').text
        ep_day = y.find('num').text
        episodelist.append(ep_title)
        episodelist.append(ep_score)
        episodelist.append(ep_day)
        print(episodelist[k],epscorelist[k],epdaylist[k])
        k+=1