# 1. 求 1 ~ 100之间,所有不能被2, 3, 5, 7 整除的数的和
#    (跳过能整除的,剩下的就是不能整除的)

s = 0

for x in range(1, 101):
    if x % 2 == 0:
        continue
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 7 == 0:
        continue
    s += x

print('和是:', s)


