

# 此示例示意函数的嵌套定义
def fn_outter():
    print("fn_outter() 被调用")

    def fn_inner():
        print("fn_inner 被调用")

    fn_inner()  #调用嵌套函数 fn_nner
    fn_inner()  # 第二次调用
    print('fn_outter() 调用结束')
    return fn_inner

fn_outter()  # 调用外层函数
# fn_inner()  # 不可以调用
fx = fn_outter()
fx()
