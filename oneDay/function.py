# coding=utf-8
"""
函数：用来完成某些重复性的动作所组成的一系列集合
参数：用来向函数中传递数据的变量

#定义函数
#1>无参无返
def add():
    a=input("请输入一个整数a:\n")
    b=input("请输入一个整数b:\n")
    c=a+b
    print c

#调用  函数名（）
add()

#2>有参无返
def add(a,b):  #形参
    c=a+b
    print c

#调用
add(1,10)   #实参

#3>无参有返
def add():
    a=input("请输入一个整数a:\n")
    b=input("请输入一个整数b:\n")
    c=a+b
    #返回值
    return c
#调用 - 用变量接受返回值
result = add()
print result


#4>有参有返
def add(a,b):
    c=a+b
    return c
#调用
result = add(3,9)
print result

"""
