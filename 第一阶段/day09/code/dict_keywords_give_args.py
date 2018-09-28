# dict_keywords_give_args.py


# 此示例示意 字典关键字传参
def myfun(a, b, c):
    '这是一个函数传参的示例'
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)


d1 = {'c': 300, 'b': 200, 'a': 100}

myfun(**d1)  # myfun(a=100, b=200, c=300)
# myfun(a=d1['a'], b=d1['b'], c=d1['c'])  # 100-->a  200-->b  300-->c

d2 = {'c': 300, 'b': 200, 'd': 400}
myfun(**d2)
