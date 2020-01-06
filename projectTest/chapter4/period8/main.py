# -*-coding:utf-8-*-

import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    discover = testLoader.discover(start_dir='./', pattern="test*.py")
    # 生成HTML格式测试报告
    with open('TestReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title="自动化测试报告",
                                description="自动化测试")
        runner.run(discover)
