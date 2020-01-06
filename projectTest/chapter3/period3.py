# -*-coding:utf-8-*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:63342/projectAutoTest/projectHtml/chapter3/period3.html")
time.sleep(1)

# id 定位
driver.find_element_by_id('search')


# class 定位
driver.find_element_by_class_name('btn-search')

# name 定位
driver.find_element_by_name('language')

# tag 定位
driver.find_element_by_tag_name('h4')

# xPath 定位
driver.find_element_by_xpath('/html/body/div/p')

# link 定位
driver.find_element_by_link_text('Tynam')

# Partial link 定位
driver.find_element_by_partial_link_text('link定位')

# CSS 选择器定位
driver.find_element_by_css_selector('button.css')


'''------------------验证断言正确------------------'''

# id 定位
id_maxlength = driver.find_element_by_id('search').get_attribute('maxlength')
assert id_maxlength == '10'


# class 定位
class_value = driver.find_element_by_class_name('btn-search').get_attribute('value')
assert class_value == "检索"

# name 定位
name_type = driver.find_element_by_name('language').get_attribute('type')
assert name_type == "checkbox"

# tag 定位
tag_text = driver.find_element_by_tag_name('h4').text
assert tag_text == "tag定位"


# xPath 定位
xPath_text = driver.find_element_by_xpath('/html/body/div/p').text
assert xPath_text == "xPath定位"

# link 定位
link_href = driver.find_element_by_link_text('Tynam').get_attribute('href')
assert link_href == "http://localhost:63342/tynam/test"

# Partial link 定位
partial_link_text = driver.find_element_by_partial_link_text('link定位').text
assert partial_link_text == "Partial link定位"

# CSS 选择器定位
css_text = driver.find_element_by_css_selector('button.css').text
assert css_text == "CSS定位"

# 关闭浏览器
driver.close()
