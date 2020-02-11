# -*-coding:utf-8-*-


class ElementIsExist(object):
    def __init__(self, driver):
        self.driver = driver

    def is_exist(self, element):
        flag = True
        try:
            self.driver.find_element_by_css_selector(element)
            return flag

        except:
            flag = False
            return flag
