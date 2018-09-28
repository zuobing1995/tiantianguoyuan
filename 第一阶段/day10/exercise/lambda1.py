# 1. 写一个lambda表达式,创建一个函数,此函数判断
# 参数n的平方加1能否被5整除.如果能整除返回True,否
# 则返回False
#   fx = lambda n: ...
#   print(fx(3))  # True
#   print(fx(4))  # False


# fx = lambda n: (n ** 2 + 1) % 5 == 0
fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False

print(fx(3))  # True
print(fx(4))  # False
