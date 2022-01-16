# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_output
   Description :   文件写入
   Author :        Amadeus
   date：          2022/1/8
-------------------------------------------------
   Change Activity:
                   2022/1/8:
-------------------------------------------------
"""

'''
<f>.write(s) 向文件写入一个字符串或字节流

<f>.writelines(lines) 将一个元素全为字符串的列表写入文件

<f>.seek(offset) 改变当前文件操作指针的位置，offset含义如下：
0-文件开头；1-当前位置；2-文件结尾
'''

f = open(r'output.txt', 'a+', encoding='utf-8')
f.write('20220-1-08 : 测试f.write()\n')

ls = ['中国', '法国', '美国']
f.writelines(ls)
f.seek(0)
for line in f:
    print(line)
f.close()

