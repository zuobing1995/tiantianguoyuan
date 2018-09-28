# 2. 写一个函数 print_even, 传入一个参数n代表终止整数
#   打印 2 4 6 8 ... n之间的所有偶数
#   函数定义如下:
#     def print_even(n):
#        ... 此处自己完成
#   测试调用：
#   　　print_even(8)
#     2
#     4
#     6
#     8



def print_even(n):
    for i in range(2, n + 1, 2):
        print(i)



print_even(80)

