# 练习：
# 　　写一个程序，让用户输入很多个正整数，当输入小于零的
#     数时结束输入
# 　　1) 打印这些数中最大的一个数
# 　　2) 打印这些数中第二大的一个数
#   3) 删除最小的一个数
#   4) 按原来顺序打印出剩余的这些数


L = []
while True:
    x = int(input("请输入正整数:"))
    if x < 0:
        break
    L.append(x)  # 等同于 L += [x]


print('您刚才输入的是:', L)
# 先复制列表到L2中，把最大一个一个数找到，
# 打印这个最大的数，然后再删除最大的数，
# 那剩下数是最大的数就是第二大的数

zuida = max(L)
print("最大的一个数是:", max(L))
L2 = L.copy()  # 复制一份
while True:
    if zuida in L2:  # 如果最大数存在则删除，否则跳出循环
        L2.remove(zuida)    
    else:
        break
print("第二大的数是:", max(L2))

# 删除所有最小的数:
zuixiao = min(L)
while zuixiao in L:
    L.remove(zuixiao)

print('最后的结果是', L)









