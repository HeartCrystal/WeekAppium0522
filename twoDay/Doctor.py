# coding=utf-8
from twoDay.Person import Person
# 子类继承父类所有的属性和方法 子类(父类)
class Doctor(Person):
    def __init__(self, name, age, dep):
        Person.__init__(self, name, age)  # 初始化父类中的属性
        self.dep = dep
    # 自定义方法
    def operator(self, type):
        print(self.dep, '的', self.name, '做', type, '手术')

# 实例化
'''
dct=Doctor('bqe',100,'wk')
dct.operator('gsyz')
dct.takeFood('稀饭',2)
'''
# 实例化 Person
p1 = Person('zhangsan', 30)
p1.takeFood('稀饭', 2)

# 子类可以调用父类的方法,父类不能调用子类方法
