# 练习:
#   写一个函数 getminmax(a, b, c) 有三个参数
#   此函数用于返回三个数的最大值,最小值
#      形成元组后返回
#        元组格式:
#          (最小值, 最大值)

#   可以偿试上述传参方式


def getminmax(a, b, c):
    xiao = min(a, b, c)
    da = max(a, b, c)
    return xiao, da


# a = int(input("请输入第1个数: "))
# b = int(input("请输入第2个数: "))
# c = int(input("请输入第3个数: "))

# t = getminmax(a, b, c)
# t = getminmax(a=a, b=b, c=c)
L = []
for i in range(1, 4):
    L.append(int(input("请输入第%d个数: " % i)))

t = getminmax(*L)
print(t)
print("最小数是:%d, 最大数是:%d" % (t[0], t[1]))
print("最小数是:%d, 最大数是:%d" % t)
