# def <函数名>(<参数>)
#   <函数体>
#   return <返回值>

# 函数设计时可以设计可变数量参数，即不确定参数总数量
# def <函数名> (<参数>, *b)
#     <函数体>
#     return <返回值>

def fact(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s

# def fact(n, m=1)
# 函数调用时，参数可以按照位置或名称方式传递
# fact(10, 5)
# fact(m=5, n=10)

# 函数的返回值
# return保留字用来传递返回值
# 函数可以有返回值，也可以没有，可以有return,也可以没有
# return可以有多个返回值


def fact2(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m



