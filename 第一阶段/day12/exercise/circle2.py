# 练习:
#   写程序:
#     1) 输入一个圆的半径，打印出这个圆的面积
#     2) 输入一个圆的面积，打印出这个圆的半径
#       (要求用math模块内的函数和数据)


import math as m

# 1) 输入一个圆的半径，打印出这个圆的面积
r = float(input("请输入圆的半径: "))
area = m.pi * r ** 2
print("面积是:", area)

# 2) 输入一个圆的面积，打印出这个圆的半径
area = float(input("请输入圆的面积: "))
r = m.sqrt(area / m.pi)
print("半径是:", r)




