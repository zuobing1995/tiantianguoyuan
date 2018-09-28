# double_star_dict_args.py


# 此示例示意双星号字典形参
def fun(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print('kwargs=', kwargs)


fun(name='weimingze', age=35, address='北京市朝阳区')
fun(a=1, b="BBBB", c=[2, 3, 4], d=True)
fun(a=100, **{'c': 300, 'b': 200}, d=400)


