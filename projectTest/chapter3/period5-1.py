# -*-coding:utf-8-*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:63342/projectAutoTest/projectHtml/chapter3/period5-1-1.html")
time.sleep(1)

print(driver.title)
# 获得当前页面句柄
page_handle = driver.current_window_handle

# 点击 a 标签进入第二个页面
driver.find_element_by_tag_name('a').click()
time.sleep(1)

# 此时 driver 还停留在第一个页面，需要转换到第二个页面

# 获得所有窗口的句柄
handles = driver.window_handles
# 切换到第二个页面
for handle in handles:
    if handle != page_handle:
        driver.switch_to.window(handle)

print(driver.title)

driver.quit()


'''利用list的index进行切换窗口'''
"""
# -*-coding:utf-8-*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:63342/projectAutoTest/projectHtml/chapter3/period5-1-1.html")
time.sleep(1)

print(driver.title)

# 点击 a 标签进入第二个页面
driver.find_element_by_tag_name('a').click()
time.sleep(1)

# 此时 driver 还停留在第一个页面，需要转换到第二个页面

# 获得所有窗口的句柄
handles = driver.window_handles
print(handles)
# 切换到第二个页面
driver.switch_to.window(handles[1])

print(driver.title)

driver.quit()
"""