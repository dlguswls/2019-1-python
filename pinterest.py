from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options) 
driver.get('https://www.pinterest.co.kr/')
elem = driver.find_element_by_id("email")
elem.send_keys('dlskadn77@naver.com')
driver.implicitly_wait(5)
elem = driver.find_element_by_id("password")
elem.send_keys('qazwsx77')
driver.implicitly_wait(5)
elem.send_keys(Keys.RETURN)
search_box = driver.find_element_by_name("searchBoxInput")
search_box.send_keys("방탄소년단")
driver.implicitly_wait(5)
search_box.send_keys(Keys.RETURN)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
texts = soup.select('.vbI XiG > div > div > a')[0].select('href')
for x in texts:
    print(x.text.strip())
