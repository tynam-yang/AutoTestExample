# -*-coding:utf-8-*-

from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period11.html')
driver.implicitly_wait(10)

# 文件上传
# "\\" 第一个"\"为转义字符
driver.find_element_by_id('uploadFile').send_keys('D:\\Users\\testFile\\test.text')


# driver.quit()




