# recursion2.py


# 限制递归层数的示例:
def fx(n):
    print("递归进入第", n, '层')
    if n == 3:
        return
    fx(n + 1)
    print("递归退出第", n, '层')


fx(1)  # 调用
print("程序结束")












