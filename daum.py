import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.daum.net/').text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.select('.hotissue_mini a[class*=link_issue]')
ranking = soup.select('.list_mini span[class*=ir_wa]')

for rank,title in zip(ranking , title_list):
    r = ''.join(rank)
    t = ''.join(title)

    print("{}:{}".format(r, t))