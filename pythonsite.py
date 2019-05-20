from selenium import webdriver
import time

browser = webdriver.Firefox()
vrowser.geet("http://python.org")
menus = browser.find_elements_by_css_selector('.top-bar_do-not-print>ul>li')['a']

pypi = None
for m in menus:
    if m.text = "PyPI ":
        pypi = m
    print(m.text)

pypi.click()

time.sleep(5)
browser.quit()
