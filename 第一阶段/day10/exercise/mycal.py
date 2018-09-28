# 写一个计算公式的解释执行器
#   已知有如下一些函数:
#     def myadd(x, y):
#         return x + y
#     def mysub(x, y):
#         return x - y
#     def mymul(x, y):
#         return x * y
  
#     def get_fun(op):
#         .... # 此处自己实现

#   get_fun(op)函数传入字符串'加'或'+' 返回myadd
#   get_fun(op)函数传入字符串'乘'或'*' 返回mymul

#   在主函数中程序如下:
#     def main():
#        while True:
#           s = input("请输入计算公式:")  # 10 加 20
#           L = s.split()  # L=['10', '加', '20']
#           a = int(L[0])
#           b = int(L[2])
#           fn = get_fun(L[1])
#           print("结果是:", fn(a, b))  # 结果是: 30


def myadd(x, y):
    return x + y

def mysub(x, y):
    return x - y

def mymul(x, y):
    return x * y


def get_fun(op):
    if op == '加' or op == '+':
        return myadd
    if op in ('乘', '*'):
        return mymul
    if op in ("减", '-'):
        return mysub


def main():
    while True:
        s = input("请输入计算公式:")  # 10 加 20
        L = s.split()  # L=['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_fun(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30

main()