
# 2. 输入一个数,打印如下正方形(用for实现)
#    请输入: 5
#    打印:
#      1 2 3 4 5
#      1 2 3 4 5
#      1 2 3 4 5
#      1 2 3 4 5
#      1 2 3 4 5

n = int(input("请输入: "))
for line_number in range(1, n + 1):
    # print("1 2 3 4 5")
    for x in range(1, n + 1):
        print(x, end=' ')
    print()  # 换行


