# mydeco1.py


# 此示例示意装饰器函数用来包装被装饰函数
def mydeco(fn):  # <<<---- 装饰器函数
    def fx():
        print("----这是被装饰函数调用之前----")
        fn()  # 调用被装饰函数
        print("++++这是被装饰函数调用之后++++")
    return fx


@mydeco
def myfun():
    print("myfun被调用")


myfun()  # 调用myfun
# myfun()
# myfun()





