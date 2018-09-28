# star_tuple_args.py


# 此示例示意星号元组形参的用法
def func(a, b, *args):
    print('a=', a)
    print('b=', b)
    print("args =", args)


func(1, 2, 3, 4, 5)


