# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩 (0 ~ 100的整数)
#     输如果入出现异常，则让此函数返回0,否则返回用户输入的成绩

#   def get_score():
#       ....

#   score = get_score()
#   print("学生的成绩是:", score)

#   注:
#     try-except语句也可以放在函数的内部使用


# 方法2，在函数内部有可能抛出异常的函数加上try-except语句
def get_score():
    try:
        n = int(input("请输入整数(0~100): "))
    except ValueError:
        return 0  # 如果有异常发生，则直接返回0
    if 0 <= n <= 100:
        return n
    else:
        return 0


score = get_score()
print("学生的成绩是:", score)

