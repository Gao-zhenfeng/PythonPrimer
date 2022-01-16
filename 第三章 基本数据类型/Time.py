# Time库的使用 ： 处理时间的标准库
# 计算机时间的表达
# 提供获取系统时间并格式化输出功能
# 提供系统级精确计时功能，用于程序性能分析
# 三类函数
# 1. 时间获取 ： time() ctime() gmtime()
# 2. 时间格式化： strftime() strptime()
# 3. 程序计时： sleep() perf_counter()

import time


# 时间获取
# 1623832828.1122985
print(time.time())
# Wed Jun 16 16:40:28 2021
print(time.ctime())
# struct
print(time.gmtime())

# 时间格式化
# strftime(tpl, ts) : tpl是格式化模板字符串，用来定义输出效果； ts是计算机内部时间类型变量
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

# 将字符串转为时间变量
# strptime(str, tpl) : str是字符串形式的时间值； tpl是格式化模板字符串，用来定义输入效果
timeStr = '2018-01-26 12:55:20'
time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")

# 程序计时
# 测量时间：perf_counter() 两次调用计算差值, 单位是s
# 产生时间：sleep()  让程序休眠 s,单位是秒，可以是浮点数

start = time.perf_counter()
end = time.perf_counter()
print(end - start)
time.sleep(3)

