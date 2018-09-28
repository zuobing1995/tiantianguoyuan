# global_local.py

# 此示例示意全局变量和局部变量
a = 100  # 全局变量
b = 200  # 全局变量


def fx(c):  # c是局部变量
    d = 400  # d是局部变量
    print(a, b, c, d)


fx(300)
print(a, b)



