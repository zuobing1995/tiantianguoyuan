# yield.py


# 此示例示意含有yield语句的函数为生成器函数，及用yield生成整数
def myyield():
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器生成结束")


for x in myyield():
    print(x)   # 2 3 5 7

# 调用生成器函数来创建一个生成器，此生成器能生成
# 2 3 5 7 这样四个数
gen = myyield()

it = iter(gen)  # 用生成器拿到对应的迭代器
print(next(it))  # 2  访问迭代器
print(next(it))  # 3  访问迭代器
print(next(it))  # 5  访问迭代器





