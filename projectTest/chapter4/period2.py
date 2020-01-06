# -*-coding:utf-8-*-

import unittest


class TestFixture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有用例执行的前置条件 setUpClassÅ")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行的后置条件 tearDownClass")

    def setUp(self):
        print("测试用例执行的前置条件 setUp")

    def tearDown(self):
        print("测试用例执行的后置条件 tearDown")

    def test_01(self):
        print("测试用例1")

    def test_02(self):
        print("测试用例2")


if __name__ == '__main__':
    unittest.main()