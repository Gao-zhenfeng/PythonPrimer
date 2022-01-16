# 天天向上

# 0.1%的区别
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))

# 0.5% 的区别
dayfactor = 0.005
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))

# 工作日进步，休息日退步
dayup = 1.0
dayfactor = 0.01

# range(start, stop[, step])
# 默认从0开始， step缺省值为1
# range(5) = {0, 1, 2, 3, 4}
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("dayup:{:.2f}".format(dayup))

def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + df)
    return dayup

dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
