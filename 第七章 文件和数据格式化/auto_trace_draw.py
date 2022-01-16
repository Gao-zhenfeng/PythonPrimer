# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     auto_trace_draw
   Description :   接口化设计
   Author :        Amadeus
   date：          2022/1/8
-------------------------------------------------
   Change Activity:
                   2022/1/8:
-------------------------------------------------
--自动化思维：数据和功能分离，数据驱动的自动运行
--接口化设计：格式化设计接口，清晰明了
--二维数据应用：应用维度组织数据，二维数据最常用

"""

import turtle

t = turtle.Turtle()
t.pensize(5)
t.pencolor('red')

datals = []

f = open('data.txt')
for line in f:
    line = line.replace('\n', '')
    datals.append(list(map(eval, line.split(','))))
f.close()

for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][0]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

