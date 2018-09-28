# try_except.py


def div_apple(n):
    print("%d个苹果您想分给几个人?" % n)
    s = input('请输入人数: ')
    cnt = int(s)  # <<- 可能触发ValueError错误进入异常
    result = n / cnt  # <<-- 可能触ZeroDivisionError错误
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print("在try的内部语句中发生了值错误，已处理并转为正常状态")
except ZeroDivisionError:
    print('输入人数为零，分苹果失败!')

print("程序正常退出")






