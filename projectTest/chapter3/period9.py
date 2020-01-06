# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period9.html')
driver.implicitly_wait(10)

# 定位下拉框
sel = driver.find_element_by_name('language')

# 根据索引选择css
Select(sel).select_by_index('2')
time.sleep(2)
# 根据文本值选择Html
Select(sel).select_by_visible_text('Html')
time.sleep(2)

driver.quit()

