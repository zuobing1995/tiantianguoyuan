# 练习:
#   1.  写一个函数mymax, 实现返回两个数的最大值:
#   如:
#     def mymax(a, b):
#        ...
#     print(mymax(100, 200))  # 200
#     print(mymax("ABCD", "ABC"))  # ABCD

# 方法1
# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# 方法2
def mymax(a, b):
    if a > b:
        return a
    return b


# 方法3
def mymax(a, b):
    return max(a, b)

print(mymax(100, 200))  # 200
print(mymax("ABCD", "ABC"))  # ABCD

