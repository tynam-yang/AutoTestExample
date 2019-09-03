# coding=utf-8

from projectTest.chapter7.test.pages.loginPage import LoginPage
from selenium.webdriver.common.by import By


class AboutPage(LoginPage):
    """关于我们页面"""

    def about_element(self):
        """关于我们页面判断元素"""
        return self.find_element(By.CSS_SELECTOR, "#about h1")
