# 3. 输入一个数,打印如下正方形
#    请输入: 5
#    打印:
#      1 2 3 4 5
#      2 3 4 5 6
#      3 4 5 6 7
#      4 5 6 7 8
#      5 6 7 8 9

n = int(input("请输入: "))
for line_number in range(1, n + 1):
    for x in range(line_number, n + line_number):
        print("%2d" % x, end=' ')
    print() 


