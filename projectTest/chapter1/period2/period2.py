from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:63342/projectAutoTest/projectHtml/chapter1/period2/index.html")
time.sleep(1)
driver.find_element_by_id('email').send_keys('tynam@test.com')
driver.find_element_by_name('password').send_keys('123')
driver.find_element_by_id('btn-login').click()
time.sleep(30)
driver.quit()

