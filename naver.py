import requests
from bs4 import BeautifulSoup

req=requests.get('https://www.naver.com/')
print(req.text)