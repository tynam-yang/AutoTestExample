import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
"""
smtplib：用于发送邮件
MIMEText：用于编写邮件内容
MIMEMultipart：多种形态邮件主体的处理
MIMEImage：邮件中处理图片
MIMEApplication：处理附件，默认子类型是application/octet-stream
"""

# 第一步：设置登陆邮箱数据
smtp_server = 'smtp.163.com'
sender = 'xxxx@163.com'
pwd = 'xxx'
receivers = ['xxx@163.com']
"""
smtp_server：使用发送邮件的服务
sender：发件人
pwd：客户端授权登陆密码
receivers：收件人，如果发送多人可写成['xxx1@qq.com', 'xxx2@163.com']
"""


# 第二步：设置发送的内容
content = 'Autotest发送邮件'
text = MIMEText(content)
"""
text：发送的内容
MIMEText(content)：内容转化为邮件的文本内容
"""


# 第三步：使用MIMEApplication 上传 pdf 附件
file = MIMEApplication(open('D:\\py\\learning\\test\\test.txt','rb').read())
file.add_header('Content-Disposition', 'attachment', filename=('utf-8','','test.txt'))

# 使用MIMEImage 上传 img 附件
with open('D:\\py\\learning\\test\\testimg.png','rb')as fp:
    img = MIMEImage(fp.read())
    img['Content-Type'] = 'application/octet-stream'
    img['Content-Disposition'] = 'attachment;filename="testimg.png"'

# 将内容添加到附件主体中
txt = MIMEMultipart()
txt.attach(text)
txt.attach(file)
txt.attach(img)
txt['Subject'] = 'test send email'
"""
txt['Subject']：邮件名称
"""


# 第四步：登录并发送
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(smtp_server, 25)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(
        sender, receivers, txt.as_string())
    print('send success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('send mail error', e)
"""
connect(smtp_server, 25)：连接服务器，第一个参数为服务，第二个参数为端口
login(sender, pwd)：登录邮箱，参数分别是用户名和密码
sendmail(sender, receivers, txt.as_string())：发送邮件，参数分别为发送者，收件人和邮件主体
quit()：退出登录
"""