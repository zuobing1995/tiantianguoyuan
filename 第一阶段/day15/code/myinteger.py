# myinteger.py


# 此示列示意用生成器函数生成从0开始到n结束的一系列的整数
def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1


for x in myinteger(30000000000):
    print(x)  # 0 1 2


L = [x for x in myinteger(100) if x % 2 == 1]
print("L =", L)

