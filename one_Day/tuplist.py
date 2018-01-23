# coding=utf-8

# 区别:  元组不可以进行更改,列表可以进行更改操作

# 1>元组tuple:用来存储不同类型的多个数据

tup = (1, 'test1', 2, 'test2', 3, 'test3')
# 根据位置--下标--下标从0开始
print(tup[0])
# 练习: 打印test3的值
print(tup[5])
# tup[开始:结束:跨越几步] 开始:开始下标值   结束:结束的下标值+1  跨越几步:默认1步 --> # tup[下限:上限:步长]
# 需求1: 取1,'test1',2
print(tup[0:3:1])
# 需求2: 取 test1 test2
print(tup[1:4:2])
# 练习1: 输出 test1 test2  test3
print(tup[1:6:2])
# 练习2:输出 1,test2
print(tup[0:4:3])
# 练习3: 输出 test1 2 test2 3
print(tup[1:5:1])

'''
#2>列表  list
list=[1,'test1',2,'test2',3,'test3']
#print list[0:3:1]
#1)insert(i,x) 在下标为i的元素前插入x
#list.insert(3,'test4')
#print list
#2)append(x)在列表的末尾追加元素x
#ctrl +  / 可以进行多行注释
# list.append('test5')
# print list
#3)删除del:通过下标
del list[2]
print list
'''