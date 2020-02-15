# -*-coding:utf-8-*-

import unittest
from projectTest.chapter9.test.pages.aboutPage import AboutPage


class TestAbout(unittest.TestCase):
    """测试关于我们页面"""

    @classmethod
    def setUpClass(cls):
        cls.about = AboutPage()
        cls.about.login()

    @classmethod
    def tearDownClass(cls):
        cls.about.quit_driver()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_about01(self):
        """进入关于我们页面测试"""
        self.about.select_menu("关于我们")
        about = self.about.about_element()
        self.assertEqual("关于我们", about.text)


if __name__ == '__main__':
    unittest.main()