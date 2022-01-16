# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     simulation
   Description :   体育竞技分析
   Author :        Amadeus
   date：          2021/12/22
-------------------------------------------------
   Change Activity:
                   2021/12/22:
-------------------------------------------------
"""

"""
1.自顶向下：解决复杂问题的有效方法
    设计层面

2.自底向上：逐步组建复杂系统的有效测试方法
-分单元测试，逐步组装、
-按照自顶向下相反的路径操作
-直至，系统各部分以组装的思路都经过测试和验证
 执行层面
 
"""
from random import random


def printIntro():
	print("模拟两个选手A和B的某种竞技比赛")
	print("程序需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
	a = eval(input("请输入A选手的能力值（0-1）"))
	b = eval(input("请输入B选手的能力值（0-1）"))
	n = eval(input("模拟比赛的场次： "))
	return a, b, n


def printSummary(winsA, winsB):
	n = winsA + winsB
	print("竞技比赛开始，共模拟{}长比赛".format(n))
	print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
	print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def simOneGame(probA, probB):
	scoreA, scoreB = 0, 0
	serving = 'A'  # 球权
	while not gameOver(scoreA, scoreB):
		if serving == 'A':
			if random() < probA:
				scoreA += 1
			else:
				serving = 'B'
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = 'A'
	return scoreA, scoreB


def gameOver(a, b):
	return a == 15 or b == 15


def simNGames(n, probA, probB):
	winsA, winsB = 0, 0
	for i in range(n):
		scoreA, socreB = simOneGame(probA, probB)
		if scoreA > socreB:
			winsA += 1
		else:
			winsB += 1
	return winsA, winsB


def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)


main()
