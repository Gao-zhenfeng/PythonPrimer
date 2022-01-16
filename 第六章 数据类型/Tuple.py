# 元组（Tuple）是一种序列类型，一旦被创建，就不能被修改
# 使用()或tuple()创建，元素之间用，分隔
# 在实际使用时，可以使用或不使用小括号


def func():
    return 1, 2  # 实际是返回了一个元组


creature = 'cat', 'dog', 'duck', 'sheep'
print(creature)
# ('cat', 'dog', 'duck', 'sheep')
color = (0x10101010, 'blue', creature)
print(color)
# (269488144, 'blue', ('cat', 'dog', 'duck', 'sheep'))



