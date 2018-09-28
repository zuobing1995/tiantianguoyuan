# 2. 计算 1 + 3 + 5 + 7 + ..... + 99 的和
#   分别用 for语句 和 while语句 实现

s = 0  # 用于记录和
for i in range(1, 100, 2):
    s += i
print(s)

s = 0
i = 1
while i < 100:
    s += i
    i += 2
print(s)


