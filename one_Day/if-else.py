# coding=utf-8
'''
分支结构:if-else
#1>if
a=input("请输入一个数A:\n")
if a>3:
    print "51"   #一定缩进: Tab键,不要空格

#2> if-else
a=input("请输入一个数A:\n")
if a>3:
    print "51"   #一定缩进: Tab键,不要空格
else:
    print "testing"
#3> if-elif-else
格式:
if 条件:
    语句1
elif 条件2:
    语句2
elif 条件3:
    语句3
...
else:
    语句4
a=input("请输入一个数A:\n")
if a>3:
    print "51"
elif a==3:
    print "testing"
else:
    print "appium"

#练习1:输入一个数b,如果b<=2,打印此数,否则打印此数加1
b=input("请输入 B:\n")
if b<=2:
    print b
else:
    print b+1
'''
'''
#练习2:输入一个成绩grade   and且   or或
[80,100] '奖励一个iphon7'
[70,80)  '奖励三星note7'
[60,70)  '奖励一个诺基亚'
其他   '放学继续上晚自习'

grade = input("请输入一个成绩:\n")
if grade>=80 and grade<=100:
    print "奖励一个iphone7"
elif grade>=70 and grade<80:
    print "奖励一个note"
elif grade>=60and grade<70:
    print "奖励诺基亚"
else:
    print "请自习"
'''
# python语言特点:   可直接判断两次
grade = input("请输入一个成绩:\n")
grade = int(grade)
if 80 <= grade <= 100:
    print('奖励一个iphone7')
elif 70 <= grade < 80:
    print('奖励三星note7')
elif 60 <= grade < 70:
    print('奖励一个诺基亚')
else:
    print('放学继续上晚自习')