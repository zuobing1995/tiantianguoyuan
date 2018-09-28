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

i = begin
while i < end:
    print(i, end=' ')
    i += 1
else:
    print()


