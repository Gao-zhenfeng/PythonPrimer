# 文本进度条
import time

print("------执行开始------")
scale = 10
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    print("\r{:^3.0f}%[{}->{}]".format(c, a, b), end="")
    time.sleep(0.1)
print("\n------执行结束------")

# 单行动态刷新
# 不能换行到下一行
# 要能回退到首行 \r

for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.01)

scale = 50
print("\n")
print("执行开始".center(20, "="))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n" + "执行结束".center(20, '='))

