# -*-coding:utf-8-*-

import unittest, time


class TestSuit(unittest.TestCase):

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_1(self):
        print('test1')
        self.assertEqual('test1', 'test2')

    def test_2(self):
        print('test2')

    def test_3(self):
        print('test3')
