# 集合数据类型
# 集合类型各元素不能改变，不能重复，且是无序的

# 使用{}创建集合
A = {"python", 123, ("python", 123)}
# {123, 'python', ('python', 123)}

# 使用set创建集合
B = set("pypy124")
# {'1', 'p', '2', '3', 'y'}

# 集合处理方法
S = {1, 3, 4}
x = 1
S.add(x)        # 如果x不在S中，将x加到 S中
S.discard(x)    # 从集合S中移除元素x,如果x不在S中，不报错
S.remove(x)     # 移除S中的x，如果x不在S中，产生KeyError异常
S.clear()       # 移除S中的所有元素
S.pop()         # 随机取出S中的一个元素，更新S,如果S为空，产生KeyError异常
S.copy()        # 返回S的一个副本
len(S)          # 返回集合S中元素的个数
# x in S        # x在S中，返回Ture, 反之，返回False
# x not in S    # 类似
# set(x)        # 将其他类型变量转换为集合类型


# 数据去重  -- 重要操作
ls = ['p', 'p', 's', 's']
ss = set(ls)

