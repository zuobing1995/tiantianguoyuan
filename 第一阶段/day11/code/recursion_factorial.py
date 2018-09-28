# 1. 给出一个数n,写一个函数myfac(n)来计算n!(n的阶乘)
#   n! = 1*2*3*4*....*n

#     print(myfac(5))  # 120


def myfac(n):
    # 用循环来实现
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

# 用递归来实现
# 5!  = 5 * 4!
# 5!  = 5 * 4 * 3!
# 5!  = 5 * 4 * 3　* 2!
# 5!  = 5 * 4 * 3　* 2 * 1!
# 5!  = 5 * 4 * 3　* 2 * 1
# 5!  = 5 * 4 * 3　* 2
# 5!  = 5 * 4 * 6
# 5!  = 5 * 24
# 5!  = 120


def myfac(n):
    if n == 1:  # 知道1! == 1
        return 1
    # 如果n不是1,则递推到下一级求解
    return n * myfac(n - 1)


print(myfac(5))  # 120


