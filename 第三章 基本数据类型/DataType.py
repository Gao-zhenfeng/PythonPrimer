# 四种进制 整数无限制
# 十进制： 10000
# 二进制,以0b或者0B开头： 0b010, -0B101
# 八进制,以0O或0o开头： 0o123, -0O456
# 十六进制，以0x或者0X开头： 0x9a， -0X89

# 浮点数--取值范围和精度基本无限制
# round(0.1 + 0.2, 1) 1表示四舍五入后，小数的位数
# round(x, [,d]) [,d]是缺省值，默认为0

# 复数类型
z = 1.23e-4 + 89j
# x ** y 幂运算
y = 0.5
x = y ** y

# // 取除法的整数部分，即向下取整
# x // y

# 数值运算函数
int(x)
float(x)
# 商余函数，返回一个二元数组
divmod(x, y)
