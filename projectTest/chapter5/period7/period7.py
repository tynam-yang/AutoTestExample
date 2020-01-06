# -*-coding:utf-8-*-

import csv

def csv_writer():
    """CSV 文本写入"""

    # 数据data
    headers = ['code', 'name', 'ranking']
    rows = [
        (1, 'Python', 'first'),
        (2, 'Java', 'second'),
        (3, 'C', 'third')
    ]

    # 读取
    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        # 直接写入
        writer.writerows(rows)
        # 也可使用for循环进行写入
        # for row in rows:
        #     writer.writerow(row)


def csv_reader():
    """CSV 文本读取"""
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print(list(reader))


if __name__ == '__main__':
    # csv_writer()
    csv_reader()

