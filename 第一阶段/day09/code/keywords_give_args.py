# keywords_give_args.py

# 此示例示意关键字传参
def myfun(a, b, c):
    '这是一个函数传参的示例'
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)


myfun(c=33, b=22, a=11)
myfun(b=200, c=300, a=100)
myfun(a=100, b=200, c=300)


