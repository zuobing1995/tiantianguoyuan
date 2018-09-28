# 练习:
#   写一个函数 myadd,此函数中的参数列表里有两个参数x,y
#   此函数的功能是打印x+y的和
#       def myadd(...):
#          ....

#       myadd(100, 200)  # 300
#       myadd("ABC", '123')  # ABC123


# def myadd(x, y):
#     s = x + y  # 求实参的和
#     print(s)

def myadd(x, y):
    if type(x) is int:
        s = x + y  # 求实参的和
    elif type(x) is str:
        s = y
    print(s)


myadd(100, 200)  # 300
myadd("ABC", '123')  # ABC123

