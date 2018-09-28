# global3.py


# 4. global变量列表里的变量名不能出现在函数的形参列表里
v = 100

def fx(v):
    # global v  # 此处错误!!!
    v = 300

fx(200)
print(v)
