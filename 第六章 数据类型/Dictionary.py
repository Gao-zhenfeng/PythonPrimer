# dictionary (字典）是python中唯一的内置映射类型
# 键-值对 键是索引，值是数据
# 字典是键值对的集合，键值对之间无序
# 采用大括号{}和dict()创建，键值对用冒号：表示

d = {'China': 'Beijing', 'USA': 'Washington', 'France': 'Paris'}
print(d["USA"])

# 生成空字典类型变量, 不能用{}来声明集合类型的变量
c = {}
# 赋值，新增元素
c['a'] = 1
c['b'] = 2

del d['USA']  # 删除'USA'项
print(d.keys())  # dict_keys(['China', 'France'])
print(d.values())  # dict_values(['Beijing', 'Paris'])
print(d.items())  # dict_items([('China', 'Beijing'), ('France', 'Paris')])

print(d.get('China', 0))  # Beijing
print(d.pop('China', 0))  # Beijing 该项出栈
print(d.items())  # dict_items([('France', 'Paris')])
# d.popitem() 随机从字典中取出一个键值对，以元组形式返回
