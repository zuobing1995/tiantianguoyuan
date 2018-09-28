# 2. 输入任意行文字，存于列表中L中，当不输入内容直接回车后结束输入:
#    1) 打印L列表中的内容
#    2) 打印出您刚才输入了几行文字信息
#    3) 打印出您刚才输入了多少个字符数据

L = []  # 先创建一个列表容器准备放数据
while True:
    s = input("请输入: ")  # 让用户循环输入字符串
    # 等用户输入完毕后，判断这个字符串是否为空
    if s == '':
        break  # 不再输入
    L += [s]

# 1) 打印L列表中的内容
print('L=', L)

# 2) 打印出您刚才输入了几行文字信息
# print("您刚才输入了%d行文字" % len(L))
lines = 0
for _ in L:
    lines += 1
print("您刚才输入了%d行文字" % lines)

# 3) 打印出您刚才输入了多少个字符数据
char_count = 0
for aline in L:
    char_count += len(aline)

print('您刚才输入了%d个字符' % char_count)


