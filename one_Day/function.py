# coding=utf-8
'''
函数:用来完成某些重复性的动作所组成的一系列集合
参数:用来向函数中传递数据的变量
#1>无参无返
#定义
def add():
    a=input("请输入一个数A\n")
    b=input("请输入一个数B\n")
    c=a+b
    print c
#调用   函数名()
add()

#2有参无返
#定义
def add(a,b):   #形参   形式参数
    c=a+b
    print c
#调用
add(2600,20000)  #实参

#3>无参有返
#定义
def add():
    a=input("请输入一个数A\n")
    b=input("请输入一个数B\n")
    c=a+b
    #返回值
    return c
#调用
#用变量接收返回值
salary=add()
print salary
'''
# 4>有参有返
def add(a,b):
    c = a+b
    return c
salary = add(6000, 9000)
print(salary)
