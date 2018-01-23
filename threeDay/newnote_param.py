#coding=utf-8
'''
新建云笔记--参数化
'''
from appium import webdriver
# 1.手机信息
import time
import xlrd
from pymysql.tests.test_issues import reload
from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 1.手机信息
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.4.2',
    'deviceName': '127.0.0.1:22515',
    'appPackage': 'com.youdao.note',
    'appActivity': 'com.youdao.note.activity2.SplashActivity',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True'
}
# 2.启动appium
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 3.定位
time.sleep(5)
# 读取excel中的数据
wb = xlrd.open_workbook("D:\\test\\data.xls")
sh = wb.sheet_by_name("note")
r_num = sh.nrows
for i in range(1, r_num):
    title = sh.cell_value(i, 1)
    content = sh.cell_value(i, 2)
    result = sh.cell_value(i, 3)
    # 官方推荐 By.ID
    # +号
    driver.find_element(By.ID, 'com.youdao.note:id/add_note_floater_open').click()
    # 新建笔记
    driver.find_element(By.NAME, u'新建笔记').click()
    # 页面跳转+时间等待
    time.sleep(3)
    # 标题
    driver.find_element(By.ID, 'com.youdao.note:id/note_title').send_keys(title)
    time.sleep(2)
    # 正文
    driver.find_element(By.XPATH, "//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]").send_keys(content)
    time.sleep(2)
    # 完成
    driver.find_element(By.ID, 'com.youdao.note:id/actionbar_complete_text').click()
'''
#验证
#获取标题
title=driver.find_element(By.ID,'com.youdao.note:id/title').text
#获取正文
summary=driver.find_element(By.ID,'com.youdao.note:id/summary').text
print title,type(title)
print summary,type(summary)

if title=='笔记' and summary=='note':
    print 'success'
else:
    print 'fail'
'''
# 关闭app
driver.quit()

