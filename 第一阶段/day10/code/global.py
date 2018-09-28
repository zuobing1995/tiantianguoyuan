# global.py


v = 100


def fn():
    global v  # 告诉解释执行器python3, v是全局变量,不是局部变量
    v = 200


fn()
print('v=', v)  # 200