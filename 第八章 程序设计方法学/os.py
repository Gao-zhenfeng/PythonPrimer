# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     os
   Description :    os库介绍
                    os库提供通用的、基本的操作系统交互功能
                    os库是python标准库，包含几百个函数
                    常用路径操作、进程管理、环境参数等几类
   Author :        Zhenfeng Gao
   date：          2021/12/22
-------------------------------------------------
   Change Activity:
                   2021/12/22:
-------------------------------------------------
"""

# os.path子库以path为入口，用于操作和处理文件路径

# %%
import os.path as op

# %%
# 返回path在当前系统中的绝对路径
print(op.abspath(__file__)) # 交互式环境会爆出异常，因为此时__file__未生成
print(op.abspath('.')) # 返回当前目录的绝对路径

abs_path = op.abspath('os.py')
# TODO("待做")
print(abs_path)

# %%
# 归一化path的表示形式，统一用\\分隔路径
norm_path = op.normpath('E:\BOOK_PDF\Python\第三章 基本数据类型\PYE3.2-实例3-天天向上的力量v2.5.pdf')
print(norm_path)

# %%
# 返回当前程序与文件之间的相对路径（relative path）
relative_path = op.relpath('E:\Program\Python\Exercise\第五章 函数和代码复用\LocalAndGlobalVariables.py')

# %%
# 返回path的目录名称
dir_name = op.dirname('E:\Program\Python\Exercise\os.py')

# %%
# 返回path中最后的文件名称
base_name = op.basename('E:\Program\Python\Exercise\os.py')
# os.py

# %%
# 组合path与paths，返回一个路径字符串
# os.path.join(path, *paths)
op.join('D:/', 'file.txt')

# %% 路径操作

print('访问时间为： \n', op.getatime(abs_path)) # access
print('修改时间为： \n', op.getmtime(abs_path)) # modify
print('创建时间为： \n', op.getctime(abs_path)) # creat

# 获取path对应文件的大小，单位式字节
op.getsize(abs_path)

# %% os库进程管理
# 使用自己写的python程序去调用其他外部程序

'''
os.system(command)
--执行程序或命令command
--在Windows系统中，返回为cmd的调用返回信息
--可以指定输入参数，用空格隔开
'''
import os
# os.system('E:\\Program\\Python\\JlLINK\\dist\\Jlink\\Jlink.exe')
# os.system('C:\\Windows\\System32\\mspaint.exe C:\\Users\\Amadeus\\Pictures\\WallPaper\\cropped-2560-1600-1105888.jpg')

# 返回当前工作目录
path = os.getcwd()
print('当前程序操作路径：', path)
# 修改当前程序操作的路径
os.chdir('D:') # 返回值为none

os.getlogin() # 获取当前登录系统用户名称
os.cpu_count() # 获取当前系统的CPU数量  12

# 获取或改变系统环境信息
os.urandom(10) # 获取n个字节长度的随机字符串，通常用于加解密运算

os.chdir('E:\Program\Python\Exercise')
print('将路径修改至： {}'.format(os.getcwd()) )
dirs = os.listdir(os.getcwd())
for file in dirs:
    print(file)