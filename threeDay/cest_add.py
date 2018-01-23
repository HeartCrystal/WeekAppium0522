# coding=utf-8
# unittest--单元测试框架
import unittest
from threeDay.Calc import Calc

class TestAdd(unittest.TestCase):  # 继承unittest中TestCase类
    # 1>测试用例执行前的初始化工作
    def setUp(self):
        print("test start")
    # 2>测试函数
    def test_add(self):
        cc = Calc(1, 2)
        # TestCase中自带断言assertEqual
        self.assertEqual(cc.add(),3)
    def test_add2(self):
        cc = Calc(2, 2)
        # TestCase中自带断言assertEqual
        self.assertEqual(cc.add(), 4)
    # 3>结束
    def tearDown(self):
        print("test end")
