# coding=utf-8
# 类名首字母大写
class Person:
    # 属性
    def __init__(self, name="null", age=0):  # 构造方法:初始化类中的属性,给属性赋初始值
        self.name = name
        self.age = age
    # 自定义方法
    def takeTv(self,program):   # 首个单词小写,第二个单词首字母大写,  类中的方法--self,表示类自身的方法
        print('年龄为', self.age, '岁的', self.name, '正在演', program)
# 使用类中的方法
# 找对象 类名()
'''
p1=Person('jd',40)
p1.takeTv('我的前半生')
'''