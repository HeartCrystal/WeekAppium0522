# coding=utf-8
from two_day.Person1 import Person
'''
医生类 和 人类    A is B   A继承B
'''
# 子类(父类)子类可以继承父类的所有属性和方法,也可以有自己的属性方法

class Doctor(Person):
    def __init__(self, name, age, dep):
        Person.__init__(self, name, age)  # 初始化父类中的属性
        self.dep = dep
    def make(self, operation):
        print(self.dep, self.name, "做", operation)

dct = Doctor('jd', 40, '外科')
dct.make("心肺移植")
dct.takeTv('我的前半生')