from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.find_element_by_name('id').send_keys('dlskadn77')
driver.find_element_by_name('pw').send_keys('nono')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
notices = soup.select('div.p_inr>div.p_info>a>span')
for n in notices:
    print(n.text.strip())