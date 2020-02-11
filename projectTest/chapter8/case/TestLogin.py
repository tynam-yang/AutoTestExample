# -*-coding:utf-8-*-

from projectTest.chapter6.common.ExcelUtil import ExcelUtil
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import time


class Case(object):

    def __init__(self):
        pass

    def get_case(self):
        """
        获取数据
        得到有用的数据，并且使数据以邮箱地址、密码、预期结果定位、预期结果的顺序返回
        """

        # 获取 Excel 中的文件数据
        sheet = 'Login'
        file = ExcelUtil(sheet_name=sheet)
        data = file.get_data()

        # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
        email_index = data[0].index("邮箱地址")
        password_index = data[0].index("密码")
        expected_element_index = data[0].index("预期结果定位")
        expected_index = data[0].index("预期结果")

        data_length = data.__len__()
        all_case = []
        # 去除header行，和其他无用的数据
        for i in range(1, data_length):
            case = []
            case.append(data[i][email_index])
            case.append(data[i][password_index])
            case.append(data[i][expected_element_index])
            case.append(data[i][expected_index])
            all_case.append(case)
        return all_case


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        """登录步骤"""

        # 邮箱地址、密码、点击登录按钮操作
        time.sleep(1)
        if email != None:
            email_element = self.driver.find_element_by_id('ty-email')
            email_element.send_keys(email)
        time.sleep(1)

        if password != None:
            password_element = self.driver.find_element_by_id('ty-pwd')
            password_element.send_keys(password)

        time.sleep(1)
        login_btn = self.driver.find_element_by_css_selector("input[value='登  录']")
        login_btn.click()

    def login_assert(self, assert_type, assert_message):
        """登录断言"""
        time.sleep(1)
        if assert_type == 'email error':
            email_message = self.driver.find_element_by_id('ty-email-error').text
            assert email_message == assert_message

        elif assert_type == 'password error':
            passrowd_message = self.driver.find_element_by_id('ty-pwd-error').text
            assert passrowd_message == assert_message

        elif assert_type == 'login sucess' or assert_type == 'login fail':
            login_message = self.driver.switch_to.alert.text
            assert login_message == assert_message
        else:
            print("输入的断言类型不正确")


@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "file:///Users/ydj/Desktop/ydj/projectAutoTest/projectHtml/chapter6/index.html"
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url=url)

    def tearDown(self):
        self.driver.quit()

    case = Case().get_case()

    @data(*case)
    @unpack
    def test_login(self, email, password, assert_type, assert_message):
        login = Login(driver=self.driver)
        login.login(email=email, password=password)
        login.login_assert(assert_type=assert_type, assert_message=assert_message)


if __name__ == '__main__':
    unittest.main()
