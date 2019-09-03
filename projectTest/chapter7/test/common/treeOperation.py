# coding=utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


class TreeOperation(object):
    """树结构操作"""
    def __init__(self, driver):
        self.driver = driver

        # 获取tree结构
        tree_elements = [{'widget-box': By.CLASS_NAME, '#tree1>div>div': By.CSS_SELECTOR,
                          '#tree1 .tree-folder-content .tree-item-name': By.CSS_SELECTOR}, ]

        # 获取画面tree下的元素
        for tree_element in tree_elements:
            self.keys = list(tree_element.keys())
            self.values = list(tree_element.values())

            # 如果找到的父节点为空，则父节点不存在，则查找的tab不匹配
            if len(self.driver.find_elements(self.values[0], self.keys[0])) > 0:
                self.tree = self.driver.find_element(self.values[0], self.keys[0])
            else:
                print("树结构未找到")

    def get_tree1(self):
        """获取树结构第一层"""
        sleep(1)
        if len(self.tree.find_elements(self.values[1], self.keys[1])) > 0:
            tree1_elements = self.tree.find_elements(self.values[1], self.keys[1])
            return tree1_elements

    def get_tree2(self):
        """获取树结构第二层"""
        if len(self.tree.find_elements(self.values[2], self.keys[2])) > 0:
            tree2_elements = self.tree.find_elements(self.values[2], self.keys[2])
            return tree2_elements

    def tree_select(self, tree_text=[]):
        """
        数结构中选择
        :param tree_text: 必须是list格式
        :return:
        """
        if len(self.get_tree1()) == 0:
            WebDriverWait(self.driver, 20).\
                until(expected_conditions.visibility_of_element_located((self.values[0], self.keys[0])))
            trees_level1 = self.get_tree1()

            for tree_level1 in trees_level1:
                if tree_level1.text == tree_text[0]:
                    tree_level1.click()

                    trees_level2 = self.get_tree1()
                    for tree_level2 in trees_level2:
                        if tree_level2.text == tree_text[1]:
                            tree_level2.click()
                            return
                        else:
                            return
                else:
                    print('未找到元素')
                    return


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('file:///Users/ydj/Desktop/ydj/projectAutoTest/projectHtml/chapter7/period4-3/index.html')
    sleep(3)
    tab = TreeOperation(driver)
    tab.tree_select(['Personals', 'Apartments'])
    #driver.quit()
