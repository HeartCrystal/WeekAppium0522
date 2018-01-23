# coding=utf-8
"""
分支结构 if-else
格式：
1>if
if 条件:
    语句

2>if-else
if 条件:
  语句
else:
  语句
3>if-else-else
if 条件1：
    语句1
elif 条件2：
    语句2
    .....
else:
    语句N



a=input("请输入一个数：A\n")
if a>2:
    print "51"   #注意：要进行缩进，Tab按键进行缩进
else:
    print "testing"

# 练习：输入一个数b，如果b<=5,打印此数，否则打印次数加1
a=input("请输入一个数：A\n")
if a<=5:
    print a
else:
    print a+1



#练习2：输入一个正整数，如果等于3，打印这个数
c=input("请输入一个数：A\n")
if c==3:
    print c
"""

# and且 or或
# 练习3：输入一个成绩grade，[90,100] 输出等级未A,[80,90] 输出等级未B,[60,80] 输出等级未C,[0,60] 输出等级未D
# 其他 输入无效
grade = input("请输入一个数：A\n")
grade = int(grade)  # 把String转换为int
if 90 <= grade <= 100:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 60 <= grade < 80:
    print("C")
elif 0 <= grade < 60:
    print("D")
else:
    print("无效")