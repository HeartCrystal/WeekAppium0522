#coding=utf-8
#作业: 冒泡排序-->相邻的两个元素进行比较,较大的元素放在后面  [3,2,5,4,6,9,7,8,1]
list=[3,2,5,4,6,9,7,8,1]
l=len(list) #列表的长度
#print l
# for i in range(0,l-1):
#     for j in range(0,l-1-i):
#         if list[j]>list[j+1]:
#             tmp=list[j]
#             list[j]=list[j+1]
#             list[j+1]=tmp
# print list

#位置交换   A,B=B,A
for i in range(0,l-1):
    for j in range(0,l-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
