# -*-coding:utf-8-*-

import unittest, time


class TestAssert(unittest.TestCase):

    def setUp(self):
        time.sleep(1)

    def test_python_sucess(self):
        print("python提供的断言，断言成功")
        assert 1 == 1

    def test_python_fail(self):
        print("python提供的断言，断言失败")
        assert 1 > 2

    def test_unittest_sucess(self):
        print("unittest提供的断言，断言成功")
        self.assertIsNone(None)

    def test_unittest_fail(self):
        print("unittest提供的断言，断言失败")
        self.assertIn('hello1', 'hello')


if __name__ == '__main__':
    unittest.main()
