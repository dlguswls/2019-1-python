import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse

start_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=mon'

def make_toon_dict(url):
    toon_dict = dict()
    req = requests.get(url)
    bs_obj = BeautifulSoup(req.text,'html.parser')
    toon_list = bs_obj.select('ul.img_list > li')
    for toon in toon_list:
        toon_name = toon.select_one('dl > dt > a')['title']
        toon_url = toon.select_one('dl > dt > a')['href']
        link = urlparse.urljoin(start_url,toon_url)
        toon_dict[toon_name] = link
    
    return toon_dict

def parse_page_toon(url):
    req = requests.get(url)
    bs_obj = BeautifulSoup(req.text,'html.parser')
    item_list = bs_obj.select('table > tr')
    for item in item_list:
        if len(item.select('td')) == 1:
            pass
        else:
            title = item.select_one('td.title').text.strip()
            rate = item.select_one('div.rating_type > strong').text.strip()
            date = item.select_one('td.num').text.strip()
            print('제목: ' + title + ' 평점: ' + rate + ' 올린 날짜: ' + date)

def next_page_toon(page1_url):
    idx = 1
    while True:
        page_url = str(page1_url) + '&page=' + str(idx)
        parse_page_toon(page_url)
        req = requests.get(page_url)
        bs_obj = BeautifulSoup(req.text,'html.parser')
        next_page_url = str(page_url) + '&page=' + str(idx + 1)
        req2 = requests.get(next_page_url)
        bs_obj2 = BeautifulSoup(req2.text,'html.parser')
        idx += 1
        nextbutton = bs_obj2.find('a',{'class':'next'})
        if not bool(nextbutton):
            break


monday_toon_dict = make_toon_dict(start_url).items()
for toon in monday_toon_dict:
    print(toon[0])
    next_page_toon(toon[1])