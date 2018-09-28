# if2.py

# 任意输入一个数字,用程序来判断这个数是
#  正数,负数还是零

n = int(input("请输入一个数: "))
if n > 0:
    print('您输入的是正数')
elif n < 0:
    print("您输入的是负数")
else:
    print("你输入的是零")