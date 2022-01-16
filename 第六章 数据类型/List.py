# 列表（list): 列表中各元素可以随意修改
ls = ['cat', 'dog', 'tiger', 1234]
print(ls)
lt = ls  # 注意： lt只是ls的引用
print(lt)

# 修改列表：给元素赋值
ls[3] = 2222
print(ls)
# ['cat', 'dog', 'tiger', 2222]

# 删除元素
del ls[3]
print(ls)
# ['cat', 'dog', 'tiger']

# 给切片赋值
name = list("Perl")
print(name)
# ['P', 'e', 'r', 'l']
name[2:] = list("ar")
print(name)
# ['P', 'e', 'a', 'r']
name[::2] = list('ll')
print(name)
# ['l', 'e', 'l', 'r']
# 可以通过切片获得插入的效果


# 扩展
name += ls
print(name)
# ['l', 'e', 'l', 'r', 'cat', 'dog', 'tiger']


# 函数方法：增删改查

# 增
ls2 = [1, 2, 3, 4]

# 清空
ls2.clear()

# 复制，深拷贝
a = [1, 2, 3]
b = a.copy()

# 计数 count
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))  # 2

# 扩展 用一个列表扩展另一个列表
c = [1, 3, 4]
a.extend(c)  # [1, 2, 3, 1, 3, 4]

# 索引 index 在列表中查找第一次出现的索引
print(c.index(4))  # 2

# 插入 insert
c.insert(2, 'code') # 把元素插入到位置2
# 相似操作  从c[2:2] = 'code'
print(c)

# pop() : 唯一既修改列表又返回一个非None值的列表方法
# 从列表中删除一个元素（默认为最后一个元素），并返回这一元素
x = [1, 3, 4]
eleOfX = x.pop()    # 4
print(eleOfX)
print(x)            # [1, 3]
x.pop(0)            # [2]

# remove() ：删除第一个为指定值的元素，不返回任何值
y = [22, 22, 11, 11]
y.remove(11)
print(y)        # [22, 22, 11]

# reverse() : 按相反顺序排列列表中的顺序
y.reverse()
print(y)        # [11, 22, 22]


