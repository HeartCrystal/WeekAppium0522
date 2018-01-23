# coding=utf-8
from appium import webdriver
import time
"""
手机自动化-计算器软件
计算器 加法计算  3+6=9?
"""
# 1>获取手机的基本信息--并存储到字典中 desired_caps
desired_caps = {}
# a.平台名称
desired_caps['platformName'] = 'Android'
# b.android平台版本
desired_caps['platformVersion'] = '4.4.4'
# c.设备名称   查看连接设备: adb devices
desired_caps['deviceName'] = '192.168.56.101:5555'
# d.包名
# 获取包名:1> uiautomatorviewer -->开启app--拍照-右侧package
desired_caps['appPackage'] = 'com.android.calculator2'
# Activity名称
desired_caps['appActivity'] = '.Calculator'

# 启动appium,并将手机信息导入,开启app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等待时间
time.sleep(2)
# 定位  --借助uiautomatorviewer进行定位
# 3   resource-id  --> id
driver.find_element_by_id("com.android.calculator2:id/digit3").click()
# +   content-desc  --> name
driver.find_element_by_name("plus").click()
# 6   text  --> name
driver.find_element_by_name("6").click()

# =
# 获取结果-text,与预期结果进行比较
driver.find_element_by_id("com.android.calculator2:id/equal").click()
# 获取结果  class-class_name    text方法后面没有括号
result = driver.find_element_by_class_name("android.widget.EditText").text
# 判断
if int(result) == 9:
    print("测试通过")
else:
    print("测试失败")

# 关闭app
driver.quit()

# 有道云笔记--> 新建云笔记

# Activity  通过apk获取Activity
# 命令 aapt dump badging com.youdao.note_5.9.1.1_73.apk
# launchable-activity:  name:为activity名称

"""
真机:
1.数据线
2.usb调试模式
3.根据手机机型--百度下载相应的驱动
4.豌豆荚
5.adb devices
"""
