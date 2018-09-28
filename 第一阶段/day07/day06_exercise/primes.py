# 2. 计算出100以内的素数,将这些素数存于列表中,最后打
#    印出列表中的这些素数

L = []

for x in range(100):
    # 判断如果x是素数就打印,不是素数就跳过判断
    if x < 2:  # 跳过小于2的数
        continue
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        L.append(x)

print(L)



