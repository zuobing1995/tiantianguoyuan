

# 此示例示意for语句的变量的创建和绑定问题

for x in range(4, 0):
    print(x)
else:
    print("for 语句结束")

# print('x绑定', x)  # 报错


for x in range(0, 4):
    print(x)

print('x绑定', x)  # 3

