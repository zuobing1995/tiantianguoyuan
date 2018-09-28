# 1. 写一个函数mysum(n) ,此函数用来计算
#    1+2+3+4+....+n的和
#   如:
#     print(mysum(100))  # 5050


def mysum(n):
    s = 0
    for x in range(1, n + 1):
        s += x
    return s


print(mysum(100))  # 5050
print(mysum(1000))
print(mysum(10000))



