# global2.py


v = 100


def fn():
    v = 200  # 不建议在global之前来创建局部变量
    print(v)

    global v
    # v = 300
    # print(v)


fn()
print('v=', v)  # 200