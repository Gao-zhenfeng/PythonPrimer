
# 将数据输出到文件
# fp = open('E:/Program/Python/Exercise/hello.txt', 'a+')
# print('Hello World!', file=fp)
# fp.close()

# raw string 最后一个字符不能是反斜杠
# print(r'hello\n world')

# 从控制台获取一个输入
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0: -1]) - 32) / 1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0 : -1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else :
    print("输入格式错误")
