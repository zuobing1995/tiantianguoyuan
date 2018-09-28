# 1. 用生成器函数，生成素数，给出起始值begin和终止值 end, 生成begin到end范围内的素数
#   如:
#     def prime(begin, end):
#       ...

#     L=[x for x in prime(10, 20)]  #L=[11,13,17,19]

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def prime(begin, end):
    for i in range(begin, end):
        # 如果i是素数
        if is_prime(i):
            yield i


L = [x for x in prime(10, 20)]  # L=[11,13,17,19]
print(L)