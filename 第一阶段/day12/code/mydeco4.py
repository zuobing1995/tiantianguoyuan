# mydeco4.py


# 此示例示意装饰器的应用场合及功能
# ------ 以下是小李写的一个装饰器函数------
def privileged_check(fn):
    def fx(name, x):
        print("正在进行权限验证.....")
        if True:
            fn(name, x)
        else:
            print("权限验证失败")
    return fx


def message_send(fn):
    def fy(n, money):
        fn(n, money)  # 调用被装饰函数
        print("正在发送短信给", n, '...')
    return fy


# ------ 以下是魏老师写的程序-------
@message_send
@privileged_check
def savemoney(name, x):  # 存钱业务
    print(name, '存钱', x, '元')
# 实质:
# savemoney = privileged_check(savemoney)
# savemoney = message_send(savemoney)


@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')


# --------以下是调用者小张写的程序-------
savemoney('小王', 200)
# savemoney('小赵', 400)

# withdraw('小李', 500)




