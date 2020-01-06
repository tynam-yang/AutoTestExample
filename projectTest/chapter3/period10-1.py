# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period10-1.html')
driver.implicitly_wait(10)

driver.find_element_by_id('windows').find_element_by_tag_name('input').click()
time.sleep(1)
# 等待弹窗的出现
WebDriverWait(driver,20).until(EC.alert_is_present())

# 切换进 alert 弹窗
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(3)

driver.quit()

