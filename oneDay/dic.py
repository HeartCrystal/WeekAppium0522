# coding=utf-8
"""
字典{}：以键值对形式存在的数据
key:value
字典中的数据没有顺序关系
"""
# 存放学生信息
dic_zhangsan = {'name': 'zhangsan', 'age': '18', 'sex': '男'}
print(dic_zhangsan['name'])  # 通过key 取 value

del dic_zhangsan['sex']
print(dic_zhangsan)  # 通过key删除value
