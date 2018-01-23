#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
import smtplib
import sys

import time
from email.header import Header
from email.mime.text import MIMEText

from pymysql.tests.test_issues import reload

reload(sys)
sys.setdefaultencoding('utf-8')
import  unittest
'''
驱动程序
1>驱动这个运行的思路
2>选择运行的脚本
3>将脚本加入测试集
4>报告设计
5>自动发送邮件设计
6>运行脚本
'''

def creatsite():
    #d第一步：获取脚本存放的位置
    test_dir ="D:\\PycharmProjects\\framework\\script"

    #第二步:选择运行的脚本---discover(参数一,参数二)
    #参数一：脚本存放的位置
    #参数二：脚本文件名规则
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    #第三步：将脚本加入测试集
    #创建一个测试测试集

    suit = unittest.TestSuite()

    #循环遍历discover中的测试脚本，并且加入测试集
    for test_case in discover:
        suit.addTest(test_case)
    #返回测试集
    return  suit

    #第四步：报告设计
def report():
    global runner,file1,filename
    # (点)表示当前目录，获取当前时间
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = '.\\report\\'+now+'result.html'

    file1 = open(filename,'wb') #wb二进制写入方式
    #将HTMLTestRunner.py文件放到 python文件的lib目录下
    #stream 报告文件 title 报告标题 description 报告描述
    runner = HTMLTestRunner(stream=file1,title='appium_test_report',description='用例运行情况' )

#第五步：自动发送邮件设计
def sendReport(report_con):
    f = open(report_con,'rb')
    mail_body = f.read()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('appium手机自动化测试报告','utf-8')
    msg['From']  = 'testing51test@163.com' #发件人
    msg['To'] = 'testing51test@163.com'  # 收件人 ，如果是多个收件人，之间用分号分开
    smtp = smtplib.SMTP('smtp.163.com')
    smtp.login('testing51test@163.com','testing')#邮箱登录用户名和密码
    smtp.sendmail(msg['From'],msg['To'].split(';'), msg.as_string())
    smtp.quit()
    print('测试报告邮件发送成功')


#第六步，运行脚本

all_tests = creatsite()
report()
runner.run(all_tests)
file1.close()
sendReport(filename)