# namespace.py


v = 100  # 全局


def fun1():
    v = 200  # 外部嵌套函数作用域
    print("fun1.v=", v)

    def fun2():
        v = 300  # 局作用域
        print('fun2.v=', v)
    fun2()  # 调用fun2


fun1()
print("全局变量v=", v)





