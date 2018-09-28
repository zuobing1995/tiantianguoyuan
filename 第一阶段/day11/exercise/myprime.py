# 2. 用filter函数将 1~100之间所有的素数放入到列表L中
#    print(L)  # [2, 3, 5, 7, 11, ....]


def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:  # 一但整数x就一定不是素数
            return False
    return True


L = list(filter(isprime, range(100)))
print(L)

