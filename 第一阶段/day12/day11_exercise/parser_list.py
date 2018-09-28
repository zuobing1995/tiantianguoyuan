# 2. 已知有列表:
#       L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#   1) 写一个函数 print_list(lst) 打印出所有的数字
#       print_list(L)  # 3 5 8 10 13 ....
#   2) 写一个函数 sum_list(lst) 返回列表中所有数字的和
#       print(sum_list(L))  # 106
#   注:
#      type(x) 函数可以返一个对象的类型
#      如:
#         >>> type(20) is int  # True
#         >>> type([3, 5, 8]) is list  # True
#         >>> type(20) is list  # False


L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]


def print_list(lst):
    for x in lst:
        if type(x) is list:  # 是列表
            print_list(x)
        else:  # 是数字
            print(x)


print_list(L)  # 3 5 8 10 13 ....


# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is int:
            s += x
        elif type(x) is list:
            print(x)
            s += sum_list(x)  # 求 x绑定的列表的和　

    return s


print('和是:', sum_list(L))  # 106

