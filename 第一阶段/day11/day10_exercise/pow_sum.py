# 2. 给出一个数n,写一个函数计算:
#     1 + 2**2 + 3**3 + 4**4 + .... n**n的和


def f(n):
    # 方法2
    return sum(map(lambda x: x ** x, range(1, n + 1)))
    # 方法1
    # s = 0
    # for i in range(1, n + 1):
    #     s += i ** i
    # return s


print(f(3))
