# -*- coding:utf-8 -*-

# 2. 写一个生成器函数myxrange([start, ], stop[, step]) 来生成一系列整数
#   要求:
#     myxrange功能与range功能相同（不允许调用range函数)
#   用自己写的myxrange函数结合生成器表达式求1~10内奇数的平方和

def myxrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            yield start  # 生成当前数送回给迭代器next函数
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError("步长不允许为0")


for x in myxrange(1, 10, 3):
    print(x)

for x in myxrange(10, 0, -3):
    print(x)   # 10, 7, 4, 1