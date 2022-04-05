import sys

sys.setdefaultencoding('utf8')

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
browser.find_element_by_id("kw").send_keys(u"四大名著")
browser.find_element_by_id("su").click()
time.sleep(2)
browser.quit()
