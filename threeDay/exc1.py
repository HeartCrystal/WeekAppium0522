# coding=utf-8

# xlrd安装:复制xlrd至C:\Python27并解压-->dos-->进入解压后的文件夹C:\Python27\xlrd-0.9.3\
# 安装命令: python setup.py install
import xlrd

# 1.打开excel  路径用双斜线 \\
wb = xlrd.open_workbook("D:\\test\\test.xls")
'''
#2.获取sheet表
sh=wb.sheet_by_name('Sheet1')
#3.获取单元格的内部 cell_value(i,j) 第i+1行,第j+1列
user=sh.cell_value(1,0)
print user

#练习1:读第二个sheet页中第二行第二列数据
sh=wb.sheet_by_name('test2')
user=sh.cell_value(1,1)
print user

#练习2:读取第一个sheet中所有用户信息 --循环
sh=wb.sheet_by_name('Sheet1')
for i in range(1,5):
    user=sh.cell_value(i,0)
    print user
'''
# 练习3:读取第一个sheet中用户名和密码,(密码如果为空,直接输出;如果不为空则转换成整型)
sh = wb.sheet_by_name('Sheet1')
r_num = sh.nrows
print(r_num)
for i in range(1, r_num):
    user = sh.cell_value(i, 0)
    passwd = sh.cell_value(i, 1)
    if passwd == '':
        print(user, passwd)
    else:
        print(user, int(passwd))