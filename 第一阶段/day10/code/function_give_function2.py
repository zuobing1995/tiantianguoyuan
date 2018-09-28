# function_give_function.py


# 此示例示意一个函数可以作为别一个函数的实参传入另一个函数中
def goodbye(L):
    for x in L:
        print("再见", x)

def hello(L):
    for x in L:
        print("你好", x)

def do_things(fn, L):
    fn(L)

do_things(goodbye, ['Tom', 'Jerry', 'Spike'])
