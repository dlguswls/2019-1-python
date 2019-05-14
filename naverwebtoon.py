import requests
from bs4 import BeautifulSoup

r = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
soup = BeautifulSoup(r.text, 'html.parser')

comics = soup.select('.list_area.daily_img > ul >li')
episodes = soup.select('.tit_area.view')
titlelist = []
linklist = []
scorelist = []
episodelist = []
epscorelist = []
epdaylist = []
i=0, k=0
for x in comics:
    title = x.find('a').get('title')
    link = x.find('a').get('herf')
    score = x.find('.rating_type > span > strong')
    titlelist.append(title)
    linklist.append(link)
    scorelist.append(score)
    print(titlelist[i],linklist[i],scorelist[i]
    i+=1
    for y in episodes:
        ep_title = y.find('h3').text
        ep_score = y.find('span').get('strong')
        ep_day = y.find('dl>dt>dd').get('date')
        episodelist.append(ep_title)
        episodelist.append(ep_score)
        episodelist.append(ep_day)
        print(episodelist[k],epscorelist[k],epdaylist[k])
        k+=1
