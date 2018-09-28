# raise.py


def make_except():
    print("开始")
    # raise ValueError  # 故意发送一个错误通知
    # e = ValueError("这是故意制作的一个错误！")
    # raise e
    raise ZeroDivisionError

    print("结束")


try:
    make_except()
except ValueError as err:
    print("make_except 发出了ValueError类型的错误，已捕获")
    # 错误的原因如何获得?
    print("错误的值是:", err)


print("程序结束")


