# -*-coding:utf-8-*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:63342/projectAutoTest/projectHtml/chapter3/period4.html")
time.sleep(1)

# 得到所有的多选框
checkboxs = driver.find_elements_by_tag_name('input')

# 将所有的多选框进行勾选
for checkbox in checkboxs:
    # 去除已经被勾选的复选框
    if checkbox.get_attribute('checked') is None:
        checkbox.click()
        time.sleep(1)


time.sleep(10)

driver.close()
