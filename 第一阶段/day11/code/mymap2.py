# mymap2.py


# 生成一个可迭代对象，此可迭代对象能够提供:
#   1**4, 2**3, 3**2, 4**1
def mypow(x, y):
    return x ** y


for i in map(mypow, [1, 2, 3, 4], (4, 3, 2, 1)):
    print(i)

print('-------------')
for i in map(pow, [1, 2, 3, 4], (4, 3, 2, 1)):
    print(i)

print("=============")
for i in map(pow,
             [1, 2, 3, 4],
             (4, 3, 2, 1),
             range(5, 1000)):
    print(i)  # 1%5  8%6 9%7 4%8




