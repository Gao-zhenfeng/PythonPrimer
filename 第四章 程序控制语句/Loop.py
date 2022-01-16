# 程序的循环结构

# for <循环变量> in <遍历结构> :
#      <语句块>
# 每次循环，所获得元素放入循环变量，并执行一次语句块

# 计数循环(N)次
# for i in range(N)
#   <语句块>

# for i in range(5):
#     print(i)

# for i in range(M, N, K)
# 1, 2, 3, 4, 5
# for i in range(1, 6):
#     print(i)

# 1, 3, 5
# for i in range(1, 6, 2):
#     print(i)

# string traverse loop
# for c in s:
for c in "Python":
    print(c, end=",")

# 列表遍历循环
# for item in ls:
for item in [123, "Py", 456]:
    print(item, end=" ")

# 文件遍历循环

# 循环的扩展 else
# for <循环变量> in <遍历结构>:                     while <条件> :
#     <语句块1>                                          <语句块1>
# else:                                           else:
#     <语句块2>                                          <语句块2>

# 当循环没有被break语句退出时，执行else语句块
# else语句块作为"正常"完成循环的奖励



