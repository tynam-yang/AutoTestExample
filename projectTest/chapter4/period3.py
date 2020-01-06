# -*-coding:utf-8-*-

import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        print("测试用例开始执行")

    def tearDown(self):
        print("测试用例执行结束")

    def add(self, a, b):
        return a+b

    def test_add(self):
        print("test开头的方法")
        result = self.add(2, 3)
        assert result == 5

    def add_test(self):
        print("非test开头的方法")
        result = self.add(2, 3)
        assert result == 5


if __name__ == '__main__':
    unittest.main()