# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_processing
   Description :   文件的打开与关闭与读取
   Author :        Amadeus
   date：          2021/12/26
-------------------------------------------------
   Change Activity:
                   2021/12/26:
-------------------------------------------------
"""
# 文件路径尽量用// 或 raw字符串
# <变量名> = open(<文件名>， <打开模式>)

f = open(r'E:\Program\Python\Exercise\第七章 文件和数据格式化\file_data_format.txt', encoding='utf-8')  # 默认是文本模式、只读模式
# f = open('file_data_format.txt', 'rt')  # 同默认值
# f = open('file_data_format.txt', 'w')  # 文本形式、覆盖写模式，文件不存在则创建，存在则覆写
# f = open('file_data_format.txt', 'wb')  # 二进制形式，覆盖写模式，文件不存在则创建，存在则覆写
# f = open('file_data_format.txt', 'x')  # 文本形式、创建写模式，文件不存在则创建，存在则返回FileExistsError
# f = open('file_data_format.txt', 'a+')  # 文本形式、追加写模式+读文件

# 文件内容的读取
s = f.read()  # 读入全部内容，如果给出参数，读入前size长度
# <f>.read.line(size=-1) # 读入一行内容，如果给出参数，size是从文件中读取的字符数
print(s)    # 此时指针已经到了文件结尾

# 读入文件所有行，以每行元素形成列表,如果给出参数，读入前hint行
# <f>.readlines(hint=-1)

# <f>.read.line(size=-1) # 读入一行内容，如果给出参数，size是从文件中读取的字符数
f.seek(0)
first_line = f.readline()
print('第一行为: {}'.format(first_line))

f.seek(0)
three_lines = f.readlines()
for line in three_lines:
    print("前三行为: " + line)
f.close()



