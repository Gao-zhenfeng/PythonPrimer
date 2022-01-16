# 程序的分支结构

# 二分支结构的紧凑形式
# <expression1> if <condition> else <expression2>
guess = eval(input("请输入一个数："))
print("猜{}了".format("对" if guess == 99 else "错"))

# 多分支形式 if: elif: else:
score = eval(input("请输入分数（1~100）："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'NOT PASS'
print("输入成绩的级别{}".format(grade))

# 保留字 and or not

# 异常信息
# try :
#   <语句块1>
# except :
#   <语句块2>
# else :
#   <语句块3>          -else对应的语句块3在不发生异常时执行
# finally ：
#   <语句块4>          - finally对应语句一定会执行




