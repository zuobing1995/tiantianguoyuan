
# 2. 分三次输入当前的小时,分钟,秒数
#    在终端打印出距离 0:0:0 过了多少秒

hour = input("请输入小时: ")
hour = int(hour)  # 将输入的字符串数据转换为整数

minute = int(input("请输入分钟: "))
second = int(input("请输入秒数: "))

s = hour * 60 * 60 + minute * 60 + second
print("距离凌晨过了", s, '秒')
