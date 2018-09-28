# 2. 打印 1 ~ 20 的整数,每行打印5个,打印四行,
#   如:
#      1 2 3 4 5
#      6 7 8 9 10
#      ....
#   提示:
#     可以将if语句嵌入到while语句中来实现换行

i = 1
while i <= 20:
    print(i, end=' ')
    if i == 5:
        print()  # 换行
    if i == 10:
        print()  # 换行
    if i == 15:
        print()  # 换行
    if i == 20:
        print()  # 换行
    i += 1
else:
    print()  # 换行
    # print(end='\n')  # 换行