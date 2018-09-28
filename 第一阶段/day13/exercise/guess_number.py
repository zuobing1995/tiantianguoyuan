# 练习:
#   １．猜数字游戏:
#     随机生成一个0~100之间的一个整数，用变量x绑定　
#     　　让用户输入一个整数用y绑定,输出猜数字的结果:
#         如果y等于生成的数x,则提示'您猜对了', 并退出程序
#         如果y大于x,则提示用户'您猜大了'
#         如果y小于x,则提示用户'您猜小了'，并继续猜
#     　　直到猜对为止，显示用户猜数字的次数后退出程序


import random
x = random.randrange(101)

count = 0  # 用来记录猜测次数

while True:
    y = int(input("请输入: "))
    count += 1  # 次数加1
    if y == x:
        print("您猜对了")
        break
    elif y > x:
        print('您猜大了')
    elif y < x:
        print('您猜小了')

print("您猜了%d次" % count)


