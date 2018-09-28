# function_give_function.py


# 此示例示意一个函数可以作为别一个函数的实参传入另一个函数中
def f1():
    print("hello f1")

def f2():
    print('hello f2')

def fx(fn):
    print(fn)  # < function f1 at 0xXXXXXXX>
    fn()  # 调用fn绑定的函数

fx(f1)  # 请问是如何执行的?
fx(f2)



