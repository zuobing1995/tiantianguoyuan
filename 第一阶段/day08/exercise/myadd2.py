# 练习:
#   写一个函数myadd2, 实现返回两个数的和:
#     如:
#       def myadd(a, b):
#           .... # 此处自己实现

#     #测试代码如下:
#       a = int(input("请输入第一个数: "))
#       b = int(input("请输入第二个数: "))
#       print("您输入的两个数之和是: ", myadd(a, b))


def myadd(a, b):
    s = a + b
    # print(s)
    return s


a = int(input("请输入第一个数: "))
b = int(input("请输入第二个数: "))
print("您输入的两个数之和是: ", myadd(a, b))

print(s)  # 错的
