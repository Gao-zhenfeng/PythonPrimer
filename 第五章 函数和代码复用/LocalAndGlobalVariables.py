# 局部变量和全局变量

n, s = 10, 100

# 在函数中声明全局变量 global


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fact(n), s)


# 规则2：局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F", "f"] # 通过使用[]真实创建了一个全局变量列表ls


def func(a):
    ls.append(a)    # 此处为传指针，ls未真实创建，等同于全局变量
    return


func("C")
print(ls)   # 全局变量被修改

ls = ["F", "f"]


def func2(a):
    ls = []
    ls.append(a)    # 此处为传指针，ls未真实创建，等同于全局变量
    return


func2("C")
print(ls)


