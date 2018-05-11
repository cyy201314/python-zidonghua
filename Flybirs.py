# coding=utf-8

'''from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': '86c8b235',

                'platformVersion': '6.0.1',

                # apk包名

                'appPackage': 'com.taobao.taobao ',
                # apk的launcherActivity

                'appActivity': 'com.taobao.tao.welcome.Welcome',
                #'appActivity': 'com.github.moduth.blockcanary.ui.DisplayActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)'''


# coding=utf-8

'''from appium import webdriver

import time

desired_caps = {

                'platformName': 'Android',

                'deviceName': '86c8b235',

                'platformVersion': '6.0.1',

                'appPackage': 'com.topband.straybirdslock',

                'appActivity': 'com.topband.straybirdslock.AppStartActivity',

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠五秒等待页面加载完成

time.sleep(5)'''

# coding:utf-8
import smtplib
from email.mime.text import MIMEText

# ----------1.跟发件相关的参数------
smtpserver = "smtp.163.com"            # 发件服务器
port = 0                                            # 端口
sender = "18825113763@163.com"                # 账号
psw = "lp201314qq"                         # 密码
receiver = "2729713016@qq.com"        # 接收人


# ----------2.编辑邮件的内容------
subject = "这个是主题163"
body = '<p>这个是发送的163邮件</p>'  # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "2729713016@qq.com"
msg['subject'] = subject

# ----------3.发送邮件------
smtp = smtplib.SMTP()
smtp.connect(smtpserver)                                  # 连服务器
smtp.login(sender, psw)                                     # 登录
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()                                                         # 关闭
