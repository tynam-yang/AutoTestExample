# -*-coding:utf-8-*-

import os, time
import unittest
from projectTest.chapter9.utils.HTMLTestRunner import HTMLTestRunner



class Main:

    def get_all_case(self):
        """导入所有的用例"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        case_path = current_path + '/../case/'
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        print(discover)
        return discover

    def set_report(self, all_case, report_path=None):
        """设置生成报告"""
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            report_path = current_path + '/../../report/'
        else:
            report_path = report_path

        # 获取当前时间
        # now = time.strftime("%Y-%m-%d %H：%M", time.localtime(time.time()))
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="年", m="月", d="日", h="时", M="分", s="秒")
        # 标题
        title = u"TYNAM后台管理系统"
        # 设置报告存放路径和命名
        report_abspath = os.path.join(report_path, title + now + ".html")
        # 测试报告写入
        fp = open(report_abspath, "wb")
        runner = HTMLTestRunner(stream=fp, title=title)
        runner.run(all_case)
        fp.close()
        return

    def run_case(self, report_path=None):
        all_case = self.get_all_case()
        self.set_report(all_case, report_path)


if __name__ == '__main__':
    Main().run_case()
