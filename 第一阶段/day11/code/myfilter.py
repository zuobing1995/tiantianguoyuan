# myfilter.py


# 此函数判断x是否为奇数，如果为奇数返回True,否则返回False
def isodd(x):
    return x % 2 == 1

for x in filter(isodd, range(10)):
    print(x)   # 1 3 5 7 9

L = list(filter(isodd, range(10)))   # L = [1, 3, 5, 7, 9]
print("L =", L)