# with3.py


# 此示例示意自定义的对象加入__enter__ 和 __exit__ 方法,让A类的对象能够使用with使用语句
class A:
    '''此类的对象可以用于with语句进行管理'''
    def __enter__(self):
        print("此方法是在with语句内执行的")
        return self  # self将 被 with 中的as 变量绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''exc_type 用来绑定错误类型,当没有异常发生时绑定None
           exc_val 用来绑定错误对象,当没有发生异常时绑定None
           exc_tb 用来绑定TraceBack对象,当没有异常时绑定None
        '''
        if exc_type is None:
            print("您已离开with语句,离开时没有发生任何异常")
        else:
            print("您已离开with语句")
            print("错误类型是:", exc_type)
            print("错误对象是:", exc_val)
            print('Traceback:', exc_tb)


with A() as a:
    print("这是with语句内部的输出")
    int(input("请输入整数: "))


print("程序正常结束")


