# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩 (0 ~ 100的整数)
#     输如果入出现异常，则让此函数返回0,否则返回用户输入的成绩

#   def get_score():
#       ....

#   score = get_score()
#   print("学生的成绩是:", score)

#   注:
#     try-except语句也可以放在函数的内部使用



def get_score():
    n = int(input("请输入整数(0~100): "))
    if 0 <= n <= 100:
        return n
    else:
        return 0


# 方法1，在调用的地方加入导常处理语句，然后进行处理
try:
    score = get_score()
except ValueError:
    score = 0  # 如果输入不合法，将成绩置零


print("学生的成绩是:", score)

