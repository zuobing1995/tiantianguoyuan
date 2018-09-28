# 练习:
#   1. 写程序算出1~20 的阶乘的和
#     1! + 2! + 3! + 4! + .... + 20!


def myfac(n):
    '''求阶乘'''
    s = 1
    for i in range(1, n + 1):
        s = s * i  # s *= i
    return s


def sum_factorial(n):
    # 方法2
    # return sum(map(myfac, range(1, n + 1)))
    # 方法1
    s = 0
    for i in range(1, n + 1):
        s += myfac(i)  # s += n!
    return s

print(sum_factorial(20))
