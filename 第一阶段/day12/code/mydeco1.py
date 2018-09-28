# mydeco1.py


# 此示例示意装饰器函数的定义和调用及装饰原理
def mydeco(fn):  # <<<---- 装饰器函数
    def fx():
        print("fx被调用")
    return fx


# @mydeco
def myfun():
    print("myfun被调用")


# 上述 mydeco的原理是在 def myfun语句调用之后加了如下语句
myfun = mydeco(myfun)

myfun()  # 调用myfun
myfun()
myfun()

