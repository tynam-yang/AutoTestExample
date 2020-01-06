# -*-coding:utf-8-*-

from selenium import webdriver
from time import sleep
import os


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period11.html')
driver.implicitly_wait(10)

# 点击上传的按钮
driver.find_element_by_id('fileupload-btn').click()
sleep(2)

# 使用 AutoIt 进行文件上传
os.system(r'D:\\Users\\testFile\\UpLoadFile.exe')

# driver.quit()

