# 练习:
#   1. 任意输入三行文字,让这三行文字依次以20个字符
#      的宽度右对齐显示输出
#     如:
#       请输入第1行: hello world
#       请输入第2行: abcd
#       请输入第3行: a
#     输出结果为:
#              hello world
#                     abcd
#                        a

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")
print("%20s" % a)
print("%20s" % b)
print("%20s" % c)


# 做完上面的题后再思考:
#   能否以最长字符串的长度进行右对齐
#   显示(左侧填充空格)?

# 求最长的一个字符串的字符数
max_len = len(a)
if len(b) > max_len:
    max_len = len(b)
if len(c) > max_len:
    max_len = len(c)

print(" " * (max_len - len(a)) + a)
print(" " * (max_len - len(b)) + b)
print(" " * (max_len - len(c)) + c)


