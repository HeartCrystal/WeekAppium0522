# coding=utf-8
'''
新建云笔记
'''
from appium import webdriver
# 1.手机信息
import time
from pymysql.tests.test_issues import reload
from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 按住ctrl键,点击sys,加入两行代码,设置默认字符集为utf-8
# def setdefaultencoding(param):
#    return None
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
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# 3.定位
time.sleep(5)
# 官方推荐 By.ID
# +号
driver.find_element(By.ID, 'com.youdao.note:id/add_note_floater_open').click()
# 新建笔记
driver.find_element(By.NAME, u'新建笔记').click()
# 页面跳转+时间等待
time.sleep(3)
# 标题
# 输入中文,在手机信息中增加unicode键盘开启
driver.find_element(By.ID,'com.youdao.note:id/note_title').send_keys(u'笔记')
time.sleep(2)
# 正文
# xpath定位 格式: //类名[@属性名='属性值' and @属性名2='属性值2']
# driver.find_element(By.ID,'com.youdao.note:id/note_content').send_keys('note')
# driver.find_element(By.XPATH,"//android.widget.EditText[@index=\"0\"]").send_keys('note')

driver.find_element(By.XPATH, "//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]").send_keys('note')

time.sleep(2)
# 完成
driver.find_element(By.ID, 'com.youdao.note:id/actionbar_complete_text').click()
# 验证
# 获取标题
title = driver.find_element(By.ID, 'com.youdao.note:id/title').text
# 获取正文
summary = driver.find_element(By.ID, 'com.youdao.note:id/summary').text

print(title, type(title))
print(summary, type(summary))

if title == '笔记' and summary == 'note':
    print('success')
else:
    print('fail')
# 关闭app
driver.quit()
