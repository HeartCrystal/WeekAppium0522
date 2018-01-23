# coding=utf-8
"""
循环结构
1>while
#循环四要素：循环变量/循环条件/循环体/循环变量变化

i = 1   #循环变量
while i<=100:   #循环条件
    print 'hello world'  #循环体
    i+=1    #i=i+1        #循环变量变化

#练习1
i = 1
while i<=5:
    grade=input("请输入一个数：A\n")
    if 90<=grade<=100:
        print "A"
    elif 80<=grade<90:
        print "B"
    elif 60<=grade<80:
        print "C"
    elif 0<=grade<60:
        print "D"
    else:
        print "无效"
    i+=1



#2>for
for i in range(1,5):
    print "hello world"

#range(m,n) 产生一个m到n-1的序列,并且存入列表中
#range(m,n,k)产生一个m到n-1的序列,步长未k
print range(1,5,2)

#练习2:1+2+..+100 求和
sum = 0
for i in range(1,101):
    sum = sum + i
print "1+2+..+100的和为",sum


#练习3：1+3+..+99 求和
sum1 = 0
for i in range(1,101,2):
    sum1 = sum1 + i
print "1+3+..+99的和为",sum1

#练习4：2+4+..+100 求和
sum1 = 0
for i in range(2,101,2):
    sum1 = sum1 + i
print "2+4+..+100的和为",sum1


for i in range(1,11):
    if i==5:
        print "51"
        # break   #跳出整个循环
        continue #跳出本次循环，进入下次循环
    else:
        print "testing"


#遍历字符串
for i in "testing":
    print i


#遍历列表
list1=[1,2,3,'test1','test2','test3']
for i in list1:
    print i

"""
