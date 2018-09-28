# 练习:
#   已知内建函数max帮助文档为:
#     >>> help(max)
#       max(iterable) -> value
#       max(arg1, arg2, *args) -> value
#     仿造max,写一个mymax函数,功能要求与max完全相同
#     (要求,不允许调用max函数)

#     print(mymax([6, 8, 3, 5]))  # 8
#     print(mymax(100, 200))  # 200
#     print(mymax(1, 3, 5, 9, 7))  # 9


# 方法1
# def mymax(a, *args):
#     if not args:  # 元组为空,只是a绑定一个可迭代对象
#         zuida = a[0]  # 先假设第一个数最大
#         for x in a:
#             if x > zuida:
#                 zuida = x
#         return zuida
#     else:  # 调用者传入的有两个或两个以上的实参
#         zuida = a  # 先假设第一个参数最大
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida


# 方法2
# def mymax(a, *args):
#     if not args:  # 元组为空,只是a绑定一个可迭代对象
#         zuida = a[0]  # 先假设第一个数最大
#         for x in a:
#             if x > zuida:
#                 zuida = x
#     else:  # 调用者传入的有两个或两个以上的实参
#         zuida = a  # 先假设第一个参数最大
#         for x in args:
#             if x > zuida:
#                 zuida = x
#     return zuida


# 方法3
# def mymax(a, *args):
#     if not args:  # 元组为空,只是a绑定一个可迭代对象
#         return max(a)
#     else:  # 调用者传入的有两个或两个以上的实参
#         return max(a, max(args))


# 方法4
def mymax(a, *args):
    if not args:  # 元组为空,只是a绑定一个可迭代对象
        return max(a)
    else:  # 调用者传入的有两个或两个以上的实参
        return max(a, *args)


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
print(mymax(1, 3, 5, 9, 7))  # 9
