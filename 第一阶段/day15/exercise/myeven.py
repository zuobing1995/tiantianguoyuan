# 练习:
#   写一个生成器函数 myeven(start, stop) 用来生成 start开始到stop结束(不包含stop)的偶数
#   如:
#     def myeven(start, stop):
#         ....

#     for x in myeven(1, 10):
#          print(x)  # 2 4 6 8
#     L = [x ** 2 for x in myeven(1, 20)]
#     print(L)


def myeven(start, stop):
    while start < stop:
        if start % 2 == 0:
            yield start
        start += 1


for x in myeven(1, 10):
    print(x)  # 2 4 6 8
L = [x ** 2 for x in myeven(2, 20)]
print(L)
