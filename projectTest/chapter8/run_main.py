# -*-coding:utf-8-*-

"""
Created on 2019-08-23
Project: TYNAM后台管理系统
@Author: Tynam
"""

import os, time, unittest
import HTMLTestRunner


# 获取当前路径
current_path = os.path.abspath(os.path.dirname(__file__))
report_path = current_path + '/report/'

# 获取当前时间
# now = time.strftime("%Y-%m-%d %H：%M", time.localtime(time.time()))
# python3中路径中含有冒号可能会导致输出错误
now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="年", m="月", d="日", h="时", M="分", s="秒")

# 标题
title = u"TYNAM后台管理系统"

# 设置报告存放路径和命名
report_abspath = os.path.join(report_path, title + now + ".html")


def all_case():
    """导入所有的用例"""
    case_path = os.getcwd()
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="Test*.py")
    print(discover)
    return discover


if __name__ == "__main__":
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=title)
    runner.run(all_case())
    fp.close()
