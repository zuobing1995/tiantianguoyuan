# 2. 写一个函数isprime(x) 判断x是否为素数，如果为素数，返回True,否则返回False
#    如:
#      print(isprime(5))  # True
#      print(isprime(6))  # False
# 3. 写一个函数prime_m2n(m, n) 返回从m开始，到n结束范围内的素数，返回这些素数的列表，并打印．
#   如:
#     L = prime_m2n(10, 20)
#     print(L)  # [11, 13, 17, 19]
# 4. 写一个函数 primes(n)  返回指定范围内n(不包含n)的全部素数的列表，并打印这些列表
#   如:
#     L = primes(10)
#     print(L)  # [2, 3, 5, 7]
#   1) 打印100以内全部素数的和
#   2) 打印200以内全部素数的和


def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:  # 如果整数则不是素数
            return False
    return True


print(isprime(5))  # True
print(isprime(6))  # False


def prime_m2n(m, n):
    L = []  # 容器
    for x in range(m, n):
        if isprime(x):
            L.append(x)
    return L


L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


def primes(n):
    return prime_m2n(1, n)


L = primes(10)
print(L)  # [2, 3, 5, 7]
# 1) 打印100以内全部素数的和
print("100以内全部素数的和", sum(primes(100)))
# 2) 打印200以内全部素数的和
print("200以内全部素数的和", sum(primes(200)))

