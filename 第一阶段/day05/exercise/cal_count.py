# 练习:
#   1. 任意输入一段字符串，
#   　　1) 计算出输入字符'a'的个数，并打印出个数
#   　　2) 计算出空格的个数，并打印出个数
#   　　　　（要求用for语句，不允许用　str.count方法)
#     思考:
#       用while 语句能否实现上述功能

s = input("请输入一段字符串: ")
count_a = 0  # 用来记录a的个数
for c in s:
    if c == 'a':
        count_a = count_a + 1
else:  # else子句只有在可迭代对象不能提供数时才会执行
    print('a的个数是:', count_a)

count_blank = 0
for c in s:
    if c == ' ':
        count_blank += 1
print('空格的个数是:', count_blank)
