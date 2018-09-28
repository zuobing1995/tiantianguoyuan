# yield.py


# 此示例示意含有yield语句的生成器函数的调用顺序
# 生成器函数只有在next(it) 函数调用时才会执行，且遇到yield后
# 返回相应的值给next(it)函数
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成器生成结束")

gen = myyield()
it = iter(gen)
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7
print(next(it))  # StopIteration





