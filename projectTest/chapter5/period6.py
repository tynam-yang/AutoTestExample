# -*-coding:utf-8-*-

import logging
import datetime
import os


class TestLog:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # 以时间命名 log 文件名
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_name = datetime.datetime.now().strftime("%y-%m-%d %H:%M") + '.log'
        log_name = base_path + '/' + file_name

        # 将日志写入磁盘
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        self.file_handle.setFormatter(file_formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        """获取log"""
        return self.logger

    def close_handle(self):
        """关闭handle"""
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    test = TestLog()
    test.get_log()
    test.get_log().debug('test log')
    test.get_log().info('test log info')
    test.get_log().critical('test log critical')
    test.close_handle()
