# coding=utf-8
'''
excel写入
'''
import xlrd
#1.复制原来的excel变为一个新的excel
#1>进入C:\Python27\xlutils-1.7.1\xlutils-1.7.1
#2>复制xlutils到C:\Python27\Lib\site-packages
from xlutils.copy import copy
wb = xlrd.open_workbook("D:\\test\\test.xls")
new_wb = copy(wb)
# 2.获取sheet页   get_sheet(i) 获取第i+1个sheet
sh=new_wb.get_sheet(1)
# write(i,j,k)向第i+1行,j+1列,写入k值
sh.write(4, 3, 'testing')
new_wb.save('D:\\test\\test.xls')


