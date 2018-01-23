# coding=utf-8
import time
from appium import webdriver
from pymysql.tests.test_issues import reload
from selenium.webdriver.common.by import By
import unittest
import sys
import xlrd
from framework.script.public import quit
reload(sys)
sys.setdefaultencoding('utf-8')

class Anewnotes(unittest.TestCase):
    """新建云笔记"""
    def setUp(self):
        # 第一，手机基础信息
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4.4',
            'deviceName': '192.168.56.101.5555',
            'appPackage': 'com.youdao.note',
            'appActivity': 'com.youdao.note.activity2.SplashActivity',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        # 启动appium
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def test_newnote(self):
        time.sleep(5)
        # 官推荐By.ID
        # 读取excel
        wb = xlrd.open_workbook("D:\\PycharmProjects\\framework\\data\\data.xls")
        sh = wb.sheet_by_name("note")
        r_num = sh.nrows
        for i in range(1, r_num):
            title = sh.cell_value(i, 1)
            content = sh.cell_value(i, 2)
            result = sh.cell_value(1, 3)
            self.driver.find_element(By.ID, "com.youdao.note:id/add_note_floater_open").click()
            self.driver.find_element(By.ID, "com.youdao.note:id/add_note_floater_add_note").click()
            # 页面跳转+时间等待
            time.sleep(5)
            # 标题中文，在手机信息中增加unicode键盘开启
            self.driver.find_element(By.ID, "com.youdao.note:id/note_title").send_keys(title)
            self.driver.find_element(By.XPATH,
                                "//android.widget.LinearLayout[    @resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]").send_keys(
                content)
            time.sleep(2)
            # 完成
            self.driver.find_element(By.ID, "com.youdao.note:id/actionbar_complete_text").click()
        # 获取,验证
        if result == 'ok':
            if self.driver.find_element(By.NAME, title) and self.driver.find_element(By.NAME, content):
                print('success')
            else:
                print('fail')
        elif title == '':
            elem1 = self.driver.find_element(By.ID, "com.youdao.note:id/title").text
            elem2 = self.driver.find_element(By.ID, "com.youdao.note:id/summary").text
            if elem1 == elem2:
                print('success')
            else:
                print('fail')
    # d调用public文件下面的公共函数
    def tearDown(self):
        quit.logout(self)


# 程序入口
if __name__ == '__main__':
    unittest.main()


