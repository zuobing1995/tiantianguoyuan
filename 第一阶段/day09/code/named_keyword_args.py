# named_keyword_args.py


# 此示例示意命名关键字传参
def fun(*, c, d):
    print('c=', c)
    print('d=', d)


# fun(3, 4)  # 出错
fun(d=4, c=3)  # 正确


def fun2(a, b, *, c, d):  # *是位置形参和关键形参的分隔符
    print(a, b, c, d)


fun2(1, 2, c=3, d=4)


def fun3(a, b, *args, c, d):
    print(a, b, args, c, d)


fun3(11, 22, 33, 44, 55, d=400, c=300)
fun3(1, 2, **{'d': 4, 'c': 3})





