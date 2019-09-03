# coding=utf-8

from selenium.webdriver.common.by import By
from time import sleep


class MultiMenuOperation(object):
    """多级菜单操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_all_menu(self):
        """获取所有的菜单"""
        sleep(1)

        # 获取所有的tab父元素
        menu_fathers = [{'nav':By.ID, '#nav>ul>li>a':By.CSS_SELECTOR, '#nav>ul>li ul>li>a':By.CSS_SELECTOR},
                       {'nav1': By.ID, 'a': By.TAG_NAME},
                       ]

        # 获取画面显示父下的所有菜单
        menu_level = []
        for menu_father in menu_fathers:
            keys = list(menu_father.keys())
            values = list(menu_father.values())

            # 确定一级菜单的父元素在页面中出现
            if len(self.driver.find_elements(values[0], keys[0])) > 0:
                # 将第一级菜单添加到list中的第一个元素
                if len(self.driver.find_elements(values[1], keys[1])) > 0:
                    menu_level_1 = self.driver.find_elements(values[1], keys[1])
                    menu_level.append(menu_level_1)

                    # 将第二级菜单添加到list中的第二个元素
                    if len(self.driver.find_elements(values[2], keys[2])) > 0:
                        menu_level_2 = self.driver.find_elements(values[2], keys[2])
                        menu_level.append(menu_level_2)
                        return menu_level
                return menu_level

    def select_menu(self, menu_text=[]):
        """
        选择菜单
        :param menu_text: 必须是list
        :return:
        """
        menu_levels = self.get_all_menu()
        i = 0
        for menus in menu_levels:
            for menu in menus:
                if menu.text == menu_text[i]:
                    sleep(1)
                    menu.click()
                    i += 1
                    break


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter7/period4-2/index.html')
    sleep(1)
    menu = MultiMenuOperation(driver)
    menu.select_menu(["链接", "必应"])
    #driver.quit()