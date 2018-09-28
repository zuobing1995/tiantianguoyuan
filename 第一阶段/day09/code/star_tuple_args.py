# star_tuple_args.py


# 此示例示意星号元组形参的用法
def func(*args):
    print("实参的个数是:", len(args))
    print("args =", args)


func()
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4, 5, 6, 7, 8, 9)


