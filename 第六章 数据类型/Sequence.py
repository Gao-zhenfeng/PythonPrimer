# 序列（sequence）:具有先后关系的一组元素,如string, list, tuple
# 几种操作适合所有序列，包括索引、切片、相加、相乘、成员资格检查等

ls = ["python", 123, ".io"]
print(ls[::-1])  # ['.io', 123, 'python']

s = "python123.io"

print(s[::-1])  # 'oi.321nohtyp'

# 切片（slicing）:前闭后开
tag = "www.google.com"
print(tag[0:-2])    # 'www.google.c'
print(tag[4:])      # 'google.com'
print(tag[::2])     # 'wwgol.o'  可以设置步长

# 序列相加
print(s + tag)      # 'python123.iowww.google.com'
# 序列乘法
print(s * 2)        # 'python123.iopython123.io'
# 成员资格
# x in s    x not in s
database = [
    ['Gao', '1111'],
    ['Li', '2222'],
    ['Zhang', '3333'],
    ['Wang', '4444']
]
username = input("Username: ")
pin = input("PIN code: ")

if [username, pin] in database:
    print("Acess granted")
else:
    print("Acess Denied")

