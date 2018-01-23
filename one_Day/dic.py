# coding=utf-8
'''
字典{} key:value  键值对
字典中的数据无顺序
'''
# 存放学生信息
dic_zhangsan={'name': 'zhangsan', 'age': 18, 'sex': 'male'}
# 通过key取value的值
print(dic_zhangsan['age'])
# 通过key删除value值
del dic_zhangsan['sex']
print(dic_zhangsan)
