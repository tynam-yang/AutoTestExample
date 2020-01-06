# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period7.html')
time.sleep(3)

# 全选内容
driver.find_element_by_class_name('ctrl-c').send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 利用 Ctrl+C 复制
driver.find_element_by_class_name('ctrl-c').send_keys(Keys.CONTROL, 'c')
time.sleep(2)
# 利用 Ctrl+V 粘贴
driver.find_element_by_class_name('ctrl-v').send_keys(Keys.NUMPAD2, 'v')
time.sleep(4)

driver.quit()
