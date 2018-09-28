# 练习:
#   输入任意一段字符串,打印出这个字符串中出现过的字符及出现过的次数:
#     如:
#       输入: ABCDABCABA
#     打印如下:
#       A: 4次
#       B: 3次
#       D: 1次
#       C: 2次
#     注: 不要求打印的顺序

s = input("请输入: ")
d = {}  # 容器用来存储 字符(键)-个数(值)

for ch in s:
    if ch not in d:  # 第一次出现在d中
        d[ch] = 1  # 将个数置为 1
    else:  # ch之前已经出现过
        d[ch] += 1

# print(d)
for k, v in d.items():
    print(k, ':', v, '次')


