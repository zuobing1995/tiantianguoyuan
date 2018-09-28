# raise.py


def make_except():
    print("开始_make_except")
    raise ValueError("我的一个值错误!")
    print("结束....")


def get_except():
    try:
        make_except()
    except ValueError as err:
        print("错误的值是:", err)
        raise  # 重新触发刚收到的错误 等同于raise err


try:
    get_except()
except ValueError as err:
    print("get_except内部发生值错误!", err)

print("程序结束")









