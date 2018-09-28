# function_variable.py


# 此示例示意函数名fn是变量.它绑定一个函数对象
def fn():
    print("hello world!")


f1 = fn
print(fn)  # <function fn at 0x7f0df513bf28>
print(f1)  # <function fn at 0x7f0df513bf28>
print(f1())  # None


def f1():
    print("函数f1被调用")


def f2():
    print('函数f2被调用')


f1, f2 = f2, f1

f1()  # f2被调用
f2()  # f1被调用


