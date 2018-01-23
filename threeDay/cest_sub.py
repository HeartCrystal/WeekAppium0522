# coding=utf-8
# unittest--单元测试框架
import unittest
from threeDay.Calc import Calc
class TestSub(unittest.TestCase):  # 继承unittest中TestCase类
    # 1>测试用例执行前的初始化工作
    def setUp(self):
        print("test start")
    # 2>测试函数
    def test_sub(self):
        cc = Calc(2, 1)
        # TestCase中自带断言assertEqual
        self.assertEqual(cc.sub(), 1)
    def test_sub2(self):
        cc = Calc(2, 2)
        # TestCase中自带断言assertEqual
        self.assertEqual(cc.sub(), 0)
    # 3>结束
    def tearDown(self):
        print("test end")
