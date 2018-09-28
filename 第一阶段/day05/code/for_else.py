# for_else.py

# 输入一段字符串，判断这个字符串内是否有'H'这个字符，并
#   打印出结果

s = input("请输入: ")

# for ch in s:
#     if ch == 'H':
#         print(s, "中含有字符'H'")
#         break
# else:
#     print(s, "中不含有字符'H'")

# 用while 实现
i = 0  # i代表字符串的索引下标
while i < len(s):
    ch = s[i]  # 获取其中一个
    if ch == 'H':
        print(s, "中含有字符'H'")
        break
    i += 1
else:
    print(s, "中不含有字符'H'")

