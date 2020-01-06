# -*-coding:utf-8-*-
import time
import win32gui
import win32con


def upload_file(fil_path, browser="chrome"):
    """
    通过 pywin32 实现文件上传的操作
    :param filePath: 文件的绝对路径
    :param browser: 浏览器类型，缺省为 chrome
    :return:
    """
    browser_type = {
        "firefox": "文件上传",
        "chrome": "打开",
        "ie": "选择要加载的文件"
    }

    # 强制等待3s，等待弹窗出现
    time.sleep(3)

    # 根据弹窗的层级，一层一层查找定位控件元素
    # 第一层 Class="#32770",Text="打开"
    dialog = win32gui.FindWindow("#32770", browser_type[browser])
    # 向下传递，第二层 Class="ComboBoxEx32",Text=None
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    # 继续向下传递，第三层 Class="ComboBox",Text=None
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    # 第四层 文件路径输入框 Class="Edit",Text=None
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)

    # 由于打开按钮的第一层和文件路径输入框第一层相同所以可以直接使用，打开按钮 Class="Button",Text="打开(&O)"
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")

    # 将文件的绝对路径输入到文件路径输入框中
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, fil_path)
    # 点击打开按钮
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period11.html')
    driver.implicitly_wait(10)

    # 点击上传的按钮
    driver.find_element_by_id('fileupload-btn').click()
    file_path = r'D:\\Users\\testFile\\test.txt'
    upload_file(file_path)
    # driver.quit()