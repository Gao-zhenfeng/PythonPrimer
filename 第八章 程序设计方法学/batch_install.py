# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     batch_install
   Description :   自动安装多个第三方库
   Author :        Amadeus
   date：          2021/12/23
-------------------------------------------------
   Change Activity:
                   2021/12/23:
-------------------------------------------------
"""
import os

libs = {'numpy', 'matplotlib', 'pillow', 'request',
        'wheel', 'networkx', 'sympy', 'django',
        'flask', 'pyopengl', 'pypdf2', 'docopt', 'pygame'}
try:
    for lib in libs:
        os.system('pip install ' + lib)
    print("Successful")
except SystemError:
    print("Failed")
