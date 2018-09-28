# while_embed.py


# 此示例示意while语句的嵌套
# 打印 1 ~ 20 的整数,打印在一行内

j = 1
while j <= 10:
    # print('1 2 3 4 ..... 20')
    i = 1
    while i <= 20:
        print(i, end=' ')
        i += 1
    else:
        print()
    j += 1


