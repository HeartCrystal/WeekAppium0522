# coding=utf-8
# unittest--单元测试框架
import unittest
from threeDay.Calc import Calc

class TestCalc(unittest.TestCase):
    # 1.开始
    def setUp(self):
        print("test start")
    # 2.测试类中的方法
    def test_add(self):
        cc=Calc(1, 1)
        self.assertEqual(cc.add(), 2)
    def test_sub(self):
        cc = Calc(2, 1)
        self.assertEqual(cc.sub(), 1)
    # 3.结束
    def tearDown(self):
        print("test end")
# 构造测试用例集
suite = unittest.TestSuite()  # 构造出一个测试用例集合
suite.addTest(TestCalc("test_add"))  # 向测试用例集中增加测试用例
# suite.addTest(TestCalc("test_sub"))
runner = unittest.TextTestRunner()  # 构造出运行机器
# 运行测试集
runner.run(suite)