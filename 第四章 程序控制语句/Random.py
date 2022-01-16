# random 库
# 随机数种子
# 两个基本函数
# seed(a=None) 初始化给定的随机数种子，默认为当前系统时间
# eg. random.seed(10) 产生种子10对应的序列
# random() 生成一个[0.0, 1.0) 之间的小数
# random.random() 完全随机

# 如果需要再现程序实现过程，需要种子，即伪随机数
# 如果需要完全随机，不关心复现结果，不用撒种子
import random
# 撒种子，如果撒种子10，后面可以复现
random.seed(10)
print(random.random())

# 扩展函数
# randint(a, b) 生成一个[a, b]之间的整数
# randrange(m, n[,k]) 生成一个[m, n)之间以k为步长的随机整数
# getrandbits(k) 生成一个k比特长的随机整数
# uniform(a, b) 生成一个[a, b]之间的随机小数
# choice(seq) 从序列seq中随机选择一个元素
# shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列
