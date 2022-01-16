# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     one_dimensional_data
   Description :   一维数据写入处理
   Author :        Amadeus
   date：          2022/1/8
-------------------------------------------------
   Change Activity:
                   2022/1/8:
-------------------------------------------------
"""
ls = ['China', 'USA', 'Japan', 'UK']
f = open('write_1d_data.txt', 'wt')
f.write(','.join(ls))  # 把列表变为空格分隔的字符串
f.close()


