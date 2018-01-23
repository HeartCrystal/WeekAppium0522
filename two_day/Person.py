# coding=utf-8
"""
把大象放到冰箱里?
1.开门openDoor    2.放大象takeEle   3.关门 closeDoor
面向过程: c语言,注重过程 函数之间的调用
面向对象: python/java  找对象    关注'谁把门开了'  --具体
类:抽象的  具有相同属性,且能够完成某些特定动作的事物所组成的集合

class Person:  #类名首字母大写
    #属性
    name='jd'
    age=40

    #自定义方法
    def takeTv(self,program): #首个单词小写,第二个单词首字母大写,  类中的方法--self,表示类自身的方法
        print self.name,'正在演',program
#使用类中的方法
#实例化---找对象 类名()
p1=Person()
p1.takeTv('我的前半生')
"""
# 练习: 医生类Doctor  方法operator 做手术  输出:xx科室的xx做xx手术  属性:姓名,科室
class Doctor:
    name = 'jd'
    department = '外科'
    def make(self,operation):
        print(self.department, self.name, "做", operation)

d1 = Doctor()
d1.make("接骨手术")