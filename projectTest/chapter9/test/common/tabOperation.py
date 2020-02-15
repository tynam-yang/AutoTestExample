# -*-coding:utf-8-*-

from time import sleep
from projectTest.chapter9.test.common.elementIsExist import ElementIsExist


class TabOperation(object):
    """Tab操作"""
    def __init__(self, driver):
        self.driver = driver

     def get_all_tab(self):
            """获取所有的tab"""
        sleep(1)

        # 获取所有的tab父元素
        # 元素定位，我们默认取css定位
        fathers_tabs = [['.tabs1', 'a2'],
                       ['.tabs', 'a'],
                       ]

        # 获取画面显示父下的所有tab
        for father_tab in fathers_tabs:
            # 使用is_exist()方法判断父节点是否存在，如果父节点不存在，则查找的tab不匹配
            father_exist = ElementIsExist(self.driver).is_exist(father_tab[0])
            # 父节点存在，则进行操作
            if father_exist:
                father = self.driver.find_element_by_css_selector(father_tab[0])
                tabs = father.find_elements_by_css_selector(father_tab[1])
                return tabs

    def switch_tab(self, tab_text):
        """
        切换tab
        :param tab_text: 需要切换到的tab内容
        :return:
        """
        tabs = self.get_all_tab()
        for tab in tabs:
            if tab.text == tab_text:
                tab.click()
                return


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter7/period4-1/index.html')
    sleep(3)
    tab = TabOperation(driver)
    tab.switch_tab('Tab2')
    #driver.quit()
