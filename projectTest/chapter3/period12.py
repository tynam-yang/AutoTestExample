# -*-coding:utf-8-*-

import time
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_settings.popups": 0, # 禁止弹窗
    "download.default_directory": "C:\\Users\\TynamYang\\Desktop\\", # 下载目录 
}

chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period12/period12.html')
time.sleep(1)
driver.find_element_by_id('downloadFile').click()

# driver.quit()
