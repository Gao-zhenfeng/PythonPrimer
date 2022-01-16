# 八个处理字符串的方法

# 1. str.lower() 或 str.upper() : 返回字符串的副本，全部字符小写/大写
# 2. str.split(sep=None) : 返回一个列表，由str根据sep被分割的部分组成 "A, B, C".split(",") 结果为 ['A', 'B', 'C']
# 3. str.count(sub) : 返回子串sub在str中出现的次数
# 4. str.replace(old, new) : 返回字符串str的副本，所有old字串被替换为new
# 5. str.center(width[, filch]) : 字符串str根据宽度width剧中，filch可选
# 6. str.strip(chars) : 从str中去掉其左侧和右侧chars中列出的字符  " =npython=".strip("=np") 结果为 "ytho"
# 7. str.join(iter) : 在iter变量除最后元素外每个元素后增加一个str, ",".join("12345")结果为"1,2,3,4,5" 主要用于字符串分隔
# 8. 字符串的格式化
# <templates>.format(<逗号分割的参数>)
# 槽：占位信息符   {}
# ：     |   <填充>    |   <对齐>     |   <宽度>    |      <,>     |     <.精度>     |      <类型>
# 引导符号   填充字符     左对齐:<      输出宽度           数字的         浮点数小数           整数类型 b, c, d, o, x, X
#                       右对齐:>                       千位分隔符   精度或字符串最大输出长度    浮点数类型 e, E, f, %
#                       居中： ^

# "{0:=^20}".format("Python")       =======Python=======
# "{0:,.2f}".format(12345.6789)     12,345.68
print("{0:=^20}".format("Python"))
print("{0:,.2f}".format(12345.6789))
