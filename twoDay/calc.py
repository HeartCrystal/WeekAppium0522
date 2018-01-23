# coding=utf-8
'''
计算器手机自动化
'''
from appium import webdriver
import time
# 1>获取手机信息-并存储到字典中
desired_caps={}
# a.平台名称
desired_caps['platformName'] = 'Android'
# b.android版本
desired_caps['platformVersion'] = '4.4.4'
# c.设备名称
desired_caps['deviceName'] = '192.168.56.101:5555'
# d.存放包名
# 获取包名:1>通过uiautomatorviewer获取 2>通过进入手机内部 adb shell
                                     #cd data/data  -->  ls
desired_caps['appPackage']='com.android.calculator2'
# e.存放Activity名称
desired_caps['appActivity']='.Calculator'
# 2>启动Appium,并将手机信息导入
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(2)
# 例:2+5=?
# 3>定位:借助SDK中的uiautomatorviewer.bat进行定位
# resource-id-->id  "2"
driver.find_element_by_id("com.android.calculator2:id/digit2").click()
# content-desc-->name   "+"
driver.find_element_by_name('加').click()
# text-->name
driver.find_element_by_name('5').click()

driver.find_element_by_id('com.android.calculator2:id/equal').click()
# class-->class_name
# result=driver.find_element_by_class_name('android.widget.EditText').text

# //android.widget.EditText[@text=\"5\" and @content-desc=\"5\"]
# xpath -> //class[@属性名="属性值" and @属性名2="属性值2"]
result = driver.find_element_by_xpath('//android.widget.ViewSwitcher[@resource-id=\"com.android.calculator2:id/display\"]/android.widget.EditText').text

print(result)
if int(result)==7:
    print("测试通过")
else:
    print("测试失败")
# 关闭计算器
driver.quit()

# 获取activity
# 通过aapt命令
# aapt dump badging xx.apk名称
# launchable-activity   name

# 任务--将云笔记--新建云笔记

