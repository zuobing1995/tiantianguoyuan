# globals_locals.py

a = 1
b = 2
c = 3


def fn(c, d):
    e = 300
    print("locals() 返回: ", locals())
    print("globals() 返回: ", globals())
    print(c)  # 100
    print(globals()['c'])  # 3

fn(100, 200)

