# -*-coding:utf-8-*-

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=options)
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period5-3.html')
time.sleep(3)

# 内容显示
show_text = driver.find_element_by_class_name('show-text').is_displayed()
print(show_text)
# 内容未显示
hidden_text = driver.find_element_by_class_name('hidden-text').is_displayed()
print(hidden_text)


# 输入框可编辑
enabled_text = driver.find_element_by_class_name('enabled-text').is_enabled()
print(enabled_text)
# 输入框不可编辑
disabled_text = driver.find_element_by_class_name('disabled-text').is_enabled()
print(disabled_text)


# 元素被选中
selected_elm = driver.find_element_by_name('python').is_selected()
print(selected_elm)
# 元素未被选中
unselected_elm = driver.find_element_by_name('JavaScript').is_selected()
print(unselected_elm)

driver.quit()


