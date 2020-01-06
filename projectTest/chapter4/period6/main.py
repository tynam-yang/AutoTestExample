# -*-coding:utf-8-*-

import unittest


if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    discover = testLoader.discover(start_dir='./', pattern="test*.py")
    print(discover)
    runner = unittest.TextTestRunner()
    runner.run(discover)