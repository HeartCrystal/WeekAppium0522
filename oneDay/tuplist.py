# coding=utf-8
"""
元组和列表
元组：不可以进行修改
列表：可以进行修改
1>元组 tuple:存放不同类型的多个数据
tup=(1,'test1',2,'test2',3,'test3')
#读取元组中的数据--通过下标值，下标从0开始
print tup[0]
print tup[5]
print tup   #以元组方式输出
#取出 2，test2   tup【下限:上限：步长】
#下限：开始值的下标值
#上限：结束值的下标+1
#步长：跨越几步
print tup[2:4:1]
#输出 test1，test2，test3
print tup[1:6:2]
#输出1，test2
print tup[0:4:3]
#输出test1，2,test2,3
print tup[1:5:1]
"""

# 2>列表list
list1 = [1, 'test1', 2, 'test2', 3, 'test3']
print(list1[1:6:2])
# 向列表中插入一个值  insert(i,x)  在下标值为i的元素前插入元素X
# list1.insert(3,5)
print(list1)

# append  在末尾追加
# list1.append('test5')
print(list1)

# del  删除
del list1[3]
print(list1)