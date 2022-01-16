# 递归实例：字符串反转
# 将字符串反转后输出
# s[::-1]


def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:] + s[0])


