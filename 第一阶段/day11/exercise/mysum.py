# 练习:
#   用递归实现求和:
#     def mysum(n):
#         # 返回 1 + 2 + 3 + 4 + .... + n的和
#         ...

#     print(mysum(100))  # 5050


def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)


print(mysum(900))  # 5050