# -*-coding:utf-8-*-  

from projectTest.chapter7.test.pages.loginPage import LoginPage
import unittest


class TestLogin(unittest.TestCase):
    """登录测试"""

    @classmethod
    def setUpClass(cls):
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_login01(self):
        """登录成功"""
        self.login.login()


if __name__ == '__main__':
    unittest.main()
