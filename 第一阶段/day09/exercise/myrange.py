# 练习:
#   写一个myrange函数: 此函数用给定的参数,返回一个存有对应整数的列表
#   如:
#     def myrange(start, stop=None, step=1):
#         ...

#     L = myrange(5)  # L = [0, 1, 2, 3, 4]
#     L = myrange(5, 10)  # L = [5, 6, 7, 8, 9]
#     L = myrange(5, 10, 2)  # L = [5, 7, 9]
#     for x in myrange(5, 10, 2):
#         print(x)   # 5 7 9


def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start  # 让 start作用终止步
        start = 0  # 起始值设置为0
    # print("起始值:", start, '终止值:', stop, '步长:', step)
    L = []
    i = start
    if step > 0:
        while i < stop:
            L.append(i)
            i += step
    elif step < 0:  # 步长小于零
        while i > stop:  # 当i比stop大时,i是生成的数
            L.append(i)
            i += step  # i的值变小
    return L


L = myrange(5)  # L = [0, 1, 2, 3, 4]
print(L)
L = myrange(5, 10)  # L = [5, 6, 7, 8, 9]
print(L)
L = myrange(5, 10, 2)  # L = [5, 7, 9]
print(L)
for x in myrange(3, 10, 2):
    print(x)   # 3 5 7 9
print("---------------------------------")
for x in myrange(10, 0, -2):
    print(x)  # 10 8 6 4 2