# coding=utf-8
"""
#面试题目：
#1>求10的阶乘 10*9*8...1
#做法一
ride = 1
for i in range(2,11):
    ride = ride * i
print ride

#做法二
#while
i=1
ride = 1
while i<11:
    ride = ride * i
    i += 1
print ride


print range(10,5,-1)  #倒序输出
list1=[1,2,3,'test1','test2','test3']
print list1[5:3:-1]
print list1[-1:-4:-1]   #从右向左，起始值为-1

#2>求100以内能被3整除的数，并存入列表
#做法一plus = 1
list1 = []
for i in range(1,101):
    if i%3 == 0:        #取余%
        list1.append(i)
print list1

#做法二
list1 = []
i = 1
while i<=100:
    if i%3 == 0:
        list1.append(i)
    i+=1
print list1
"""

# 3>定义一个列表[1,2,8,7,6,5,3,4,9]进行冒泡排序,相邻两数进行比较,较大的数放在后面
list = [1, 2, 8, 7, 6, 5, 3, 4, 9]
l = len(list)  # 列表长度  9个元素
print(l)
for i in range(0, l-1):
    for j in range(0, l-i-1):
        print(j, i)
        if list[j] > list[j+1]:
            tmp = list[j]
            list[j] = list[j+1]
            list[j+1] = tmp
            print(list)
print(list)
# 解题思路:
# l=9   j=l-i-1
# i=0   j比较8次
# i=1   j比较7次
# i=2   j比较6次