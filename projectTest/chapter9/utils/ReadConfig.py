# -*-coding:utf-8-*-


import json


class ReadConfig(object):
    """
    读取配置文件，Excel、josn等文件的读取方法都可写在此类下
    """
    def __init__(self):
        pass

    def read_json(self, json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                data = json.load(f)
                return data
        except:
            print("文件不存在或不是json文件")


if __name__ == '__main__':
    data = ReadConfig().read_json("../config/base_data.json")
    print(data)
    print(data['base_url'], data['email'], data['password'])
