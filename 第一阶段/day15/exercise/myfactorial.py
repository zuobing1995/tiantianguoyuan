# 练习:
#   写一个生成器函数myfactorial(n)此函数用来生成n个从1开始的阶乘

#   def myfactorial(n):
#       ...

#   L = list(myfactorial(5))  # L = [1, 2, 6, 24, 120]
#                             #      1! 2! 3!  4!  5!


def myfactorial(n):
    s = 1  # 用来保存阶乘
    for x in range(1, n + 1):
        s *= x
        yield s


L = list(myfactorial(5))  # L = [1, 2, 6, 24, 120]
print(L)

print(sum(myfactorial(5)))
