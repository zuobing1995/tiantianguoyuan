# 练习:
#   写一个函数 myadd,  此函数可以计算两个,三个,四个实参的和
#   def myadd(...):
#      ....

#   print(myadd(100, 200))  # 300
#   print(myadd(100, 200, 300))  # 600
#   print(myadd(100, 200, 300, 400))  # 1000
#   print(myadd(100, 200, 300, 400, 500))  # 报错


def myadd(a, b, c=0, d=0):
    return a + b + c + d


print(myadd(100, 200))  # 300
print(myadd(100, 200, 300))  # 600
print(myadd(100, 200, 300, 400))  # 1000
# print(myadd(100, 200, 300, 400, 500))  # 报错
