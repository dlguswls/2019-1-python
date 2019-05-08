import requests
from bs4 import BeautifulSoup
 
r = requests.get('https://www.naver.com/')
soup = BeautifulSoup(r.text, 'html.parser')
list_=soup.select('ul.ah_l')[0].select('li')
for x in list_:
    print(x.text.strip())