# coding=utf-8
# 单行注释:对代码的解释说明
'''
功能:输入输出
编写人:zxd
编写日期:2017-7-22

#各种语言输出对比
java --> System.out.print()
c    --> printf()
vbs  --> msgbox
shell --> echo
python --> print

#输出-打印
print "hello 51"

#python是一种弱类型的语言
a=3  #将3赋给变量a
b=3.4
c='t'
d="testing"

print a
print b
print c
print d
print "a,b,c,d的值为",a,b,c,d

print type(a)  #type 类型
print type(b)
print type(c)
print type(d)
#标点符号:英文标点:搜狗输入法-->属性-->中文时使用英文标点

#输入
#input
e=input() #根据输入判断类型  ,如果为字符需要加""引号
print e
print type(e)
'''
# raw_input 不论输入什么类型的数据,都为str
from pip._vendor.distlib.compat import raw_input

f = raw_input("请输入F:")
print(f)
print(type(f))

"""
python raw_input() 用来获取控制台的输入。
raw_input() 将所有输入作为字符串看待，返回字符串类型。
注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
注意：python3 里 input() 默认接收到的是 str 类型。
"""



