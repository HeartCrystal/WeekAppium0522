#coding=utf-8
'''
循环结构

#1>while
#输出"hello 51" 10次
#循环的四要素:循环变量,循环条件,循环体,循环变量变化
i=1  #循环变量
while i<=10:  #循环条件
    print "hello 51" #循环体
    i=i+1  #循环变量变化
#判断成绩5次
i=0
while i<5:
    grade=input("请输入一个成绩:\n")
    if 80<=grade<=100:
        print '奖励一个iphone7'
    elif 70<=grade<80:
        print '奖励三星note7'
    elif 60<=grade<70:
        print '奖励一个诺基亚'
    else:
        print '放学继续上晚自习'
    i=i+1

#for
#range(m,n) 产生m到n-1的序列,并且存入列表
#range(m,n,k) 产生m到n-1的序列,步长为k
# print range(1,10)
# print range(1,10,2)
for i in range(1,6):
    print i
    print "hello 51"

#练习1: 计算1+2+3+...+100和  while+for
#for 循环
sum=0
for i in range(1,101):
    sum=sum+i
print "1+2+3+...+100的和为",sum

#while循环
i=1
sum=0
while i<101:
    sum=sum+i
    i+=1  # i=i+1
print "1+2+3+...+100的和为",sum
#练习2: 计算100以内偶数的和
s=0 #s为偶数的和
for i in range (2,101,2):
    s=s+i
print "100以内偶数的和为",s

#while
i=2
sum1=0
while i<101:
    sum1=sum1+i
    i=i+2
print sum1
#练习3: 求10的阶乘 10*9*8...*1
fac = 1
for i in range(1,11):
    fac = fac *i
print '10的阶乘为',fac

#倒序输出
print range(10,0,-1)
list=[1,2,3,'test1','test2']
print list[4:2:-1]
print list[-1:-3:-1]

#练习4: 求1000以内能被3整除的数,并存入列表中
list= []
for i in range(1,1001):
    if i%3 ==0:   #%取余
        list.append(i)
print list

#break/continue
for i in range(1,11):
    if i==5:
        print "51"
        #break #中断循环,跳出整个循环
        continue #跳出本次循环,继续进入下次循环
        print "51"
    else:
        print "testing"

#遍历字符串中的字符
for i in "testing":
    print i
    '''
# 遍历列表中的元素
list = [1, 2, 3, 'test1', 'test2']
for i in list:
    print(i)

# 作业: 冒泡排序-->相邻的两个元素进行比较,较大的元素放在后面
# [3,2,5,4,6,9,7,8,1]