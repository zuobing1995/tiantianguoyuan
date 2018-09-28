# L = [2, 3, 5, 7]
# for x in L:
#     print(x)  # 2 3 5 6
# 以下用迭代器来访问L列表中的元素


# L = [2, 3, 5, 7]
# it = iter(L)  # 先拿到迭代器用iter绑定
# while True:
#     try:
#         x = next(it)  # 获取一个数据并绑定到x
#         print(x)  # 2 3 5 7
#     except StopIteration:
#         break


L = [2, 3, 5, 7]
it = iter(L)  # 先拿到迭代器用iter绑定
try:
    while True:
        x = next(it)  # 获取一个数据并绑定到x
        print(x)  # 2 3 5 7
except StopIteration:
    pass
