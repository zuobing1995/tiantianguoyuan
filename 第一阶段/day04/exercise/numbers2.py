# 2. 写一个程序
#   输入一个开始的整数,用变量begin绑定
#   输入一个结束的整数,用变量end绑定
#   打印 从begin到end(不包含end) 的每个整数, 打印在一行内.
#   如:
#     请输入开始值: 8
#     请输入结束值: 100
#   打印:
#     8 9 10 11 .....    99
#   思考:
#     如何实现每5个数打印在一行内,打印多行

begin = int(input("请输入开始整数: "))
end = int(input("请输入结束整数: "))

count = 0  # 此变量用来记录已经在一行内打印多少个数字

i = begin
while i < end:
    print(i, end=' ')
    count += 1  # 打印个数+1
    if count == 5:
        print()  # 换行后
        count = 0  # 本行的个数为0
    i += 1
else:
    print()


