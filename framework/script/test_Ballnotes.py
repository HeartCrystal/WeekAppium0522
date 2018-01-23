# coding=utf-8
import time
from appium import webdriver
from pymysql.tests.test_issues import reload
from selenium.webdriver.common.by import By
import unittest
import sys
import xlrd
from framework.script.public import quit
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Ballnotes(unittest.TestCase):
    def setUp(self):
        #第一，手机基础信息
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


    def test_allnotes(self):
        driver = self.driver
        time.sleep(5)
        #截图

        driver.get_screenshot_as_file('D:\\PycharmProjects\\framework\\picture\\pic1.png')

        #切换

        driver.find_element(By.ID, 'com.youdao.note:id/doc_all').click()
        time.sleep(2)
        # 截图2
        driver.get_screenshot_as_file('D:\\PycharmProjects\\framework\\picture\\pic2.png')
        time.sleep(2)
        # 点击最新
        driver.find_element(By.ID, 'com.youdao.note:id/doc_news').click()
        time.sleep(2)
        # 截图3
        driver.get_screenshot_as_file('D:\\PycharmProjects\\framework\\picture\\pic3.png')

    def tearDown(self):
        quit.logout(self)

    if __name__ == '__main__':
        unittest.main()
