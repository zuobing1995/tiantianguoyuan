# 2. 打印 九九乘法表:
#     1x1=1
#     1x2=2 2x2=4
#     1x3=3 2x3=6 3x3=9
#     .....
#     1x9=9 ..............9x9=81

#  方法1 循环嵌套
for line in range(1, 10):  # line代表行数
    for col in range(1, line + 1):  # col 代表列
        print("%dx%d=%d" % (col, line, col * line), end=' ')
    print()  # 换行


# 方法2 函数嵌套调用
def print_aline(end):
    for col in range(1, end + 1):
        print("%dx%d=%d" % (col, end, col * end), end=' ')
    print()


def print_99():
    for line in range(1, 10):
        # 打印一行
        print_aline(line)


print_99()










