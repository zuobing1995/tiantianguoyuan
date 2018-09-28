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
except (ValueError, ZeroDivisionError):
    print("分苹果失败,苹果不分了")

# except ValueError:
#     print("分苹果失败，苹果不分了")
# except ZeroDivisionError:
#     print("分苹果失败，苹果不分了")

print("程序正常退出")






