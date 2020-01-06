# autoTest
自动化测试实例

projectHtml和projectTest目录下以chapter开头命名的目录为对应的章节。

projectHtml：示例中所使用的HTML脚本。

projectTest：示例中所产生的py文件和项目结构。

示例代码对应表：

|HTML代码|应用位置|py文件|py文件说明|
|--|--|--|--|
|projectHtml/chapter1/period2/index.html|第一章 第二节 第一个项目|projectTest/chapter1/period2/period2.py|第一个项目实例操作|
|projectHtml/chapter3/period3.html|第三章 第三节 元素定位|projectTest/chapter3/period3.py|元素定位实例操作|
|projectHtml/chapter3/period4.html|第三章 第四节 定位一组元素|projectTest/chapter3/period4.py|定位一组元素，多选框实例操作|
|projectHtml/chapter3/period5-1-1.html|第三章 第五节 12小节switch_to.window|projectTest/chapter3/period5-1.py|浏览器窗口切换|
|projectHtml/chapter3/period5-2.html|第三章 第五节 13小节滚动条操作|projectTest/chapter3/period5-2.py|滚动条操作|
|projectHtml/chapter3/period5-3.html|第三章 第六节 7小节、8小节、9小节 对象状态|projectTest/chapter3/period5-3.py|元素显示状态、输入框编辑状态、元素选中状态|
|projectHtml/chapter3/period7.html|第三章 第七节 键盘操作|projectTest/chapter3/period7.py|模拟键盘操作|
|projectHtml/chapter3/period9.html|第三章 第七节 下拉框操作|projectTest/chapter3/period9.py|下拉框选择元素|
|projectHtml/chapter3/period10-1.html|第三章 第十节 1小节、2小节 弹窗操作|projectTest/chapter3/period10-1.py|windows弹窗操作|
|--|--|projectTest/chapter3/period10-2.py|非windows弹窗操作|
|projectHtml/chapter3/period10-2.html|第三章 第十节 3小节 frame与iframe操作|projectTest/chapter3/period10-3.py|iframe操作|
|projectHtml/chapter3/period11.html|第三章 第十一节 文件上传操作|projectTest/chapter3/period11-1.py|send_keys文件上传|
|--|--|projectTest/chapter3/period11-2.py|AutoIt工具文件上传|
|--|--|projectTest/chapter3/period11-3.py|WinSpy工具文件上传|
|projectHtml/chapter3/period12/period12.html|第三章 第十二节 文件下载操作|projectTest/chapter3/period12.py|文件下载|
|--|第四章 第二节 Test fixture|projectTest/chapter4/period2.py|测试数据的准备与销毁|
|--|第四章 第三节 Test Case|projectTest/chapter4/period3.py|测试用例|
|--|第四章 第四节 断言 Assert|projectTest/chapter4/period4.py|测试断言|
|--|第四章 第六节 TestLoader|projectTest/chapter4/period6/main.py|测试用例添加进测试套件(TestSuit)|
|--|第四章 第八节 生成HTML报告|projectTest/chapter4/period8/main.py|HTML报告生成|
|--|第五章 第五节 邮件模块smtplib|projectTest/chapter5/period5.py|邮件模块smtplib的使用|
|--|第五章 第六节 日志logging|projectTest/chapter5/period6.py|日志logging模块的使用|
|--|第五章 第七节 CSV文件读写|projectTest/chapter5/period7/period7.py|CSV文件读写|
|projectHtml/chapter6/index.html|第八章 数据驱动 测试登录页面|projectTest/chapter6|数据驱动目录结构及测试py文件|
|projectHtml/chapter7/period4-1/index.html|第九章 第五节 1小节 Tab切换|--|--|
|projectHtml/chapter7/period4-2/index.html|第九章 第五节 2小节 多级菜单|--|--|
|projectHtml/chapter7/period4-6/index.html|第九章 第五节 4小节 分页|--|--|
|--|--|projectTest/chapter7|PO模型，目录结构及测试py文件|
