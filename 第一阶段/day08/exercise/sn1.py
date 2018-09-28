# 1. 编写函数fun,其功能是: 计算并返回下载多项式的值
#    Sn = 1 + 1/2 + 1/3 + 1/4 + .... + 1/n
#   函数如下：
#   　　def fun(n):
#         ...
#   print(fun(3))  # 1.8333333333333
#   print(fun(10))  # ?????????????


# def fun(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += 1 / x
#     return s

def fun(n):
    return sum([1 / x for x in range(1, n + 1)])

print(fun(3))  # 1.8333333333333
print(fun(10))  # ?????????????