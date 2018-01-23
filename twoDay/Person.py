# coding=utf-8
'''
面向过程：c语言  ：注重过程

‘例：把大象放到冰箱分几步’

面向对象：python、java  ‘找对象’  ‘找谁把门开了’  ---具体
类：具有相同属性，且能狗完成某些特定动作的事物所组成的集合
属性：类中的事物所具有的特性
方法：完成某些特定的动作    函数/操作

#类的定义  --抽象
class Person:  #首字母大写
    #属性
    name='bh'
    age=38
    #自定义方法
    def takeFood(self,food):    #方法名,第二个单词首字母大写,  类中的方法,self,表示类自身的方法
        print self.name,'吃',food #self.name表示类的属性
#使用类中的方法
#实例化-'找对象'   类名()
p1=Person()
p1.takeFood('米饭')

#练习:创建一个医生类,方法 operator 输出:xx科室的xx做xx手术  属性: 姓名,年龄,性别,科室
class Doctor:
    name='白求恩'
    dep='外科'

    def operator(self,type):
        print self.dep,'的',self.name,'做',type,'手术'
d=Doctor()
d.operator('骨髓移植')
'''

# 首字母大写
class Person:
    # 属性
    def __init__(self,name="null",age=0): #构造方法:初始化类中的属性,给属性赋初值
        self.name=name
        self.age=age
    # 自定义方法
    # 自定义方法
    # 方法名,第二个单词首字母大写,  类中的方法,self,表示类自身的方法
    def takeFood(self,food,num):
        print(self.name,'吃',num,'碗',food)  # self.name表示类的属性
# 实例化
p1 = Person('zhangsan')
p1.takeFood('米饭', 3)
'''
#练习2:修改医生
class Doctor():
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def operator(self,type):
        print self.department,'的',self.name,'做',type,'手术'
d=Doctor('白求恩','外科')
d.operator('骨髓移植')
'''
