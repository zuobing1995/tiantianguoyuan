# 2. 输入一个学生的三科成绩(只要三个数,不要求科目)
#   1) 打印出最高分是多少?
#   2) 打印出最低分是多少?
#   3) 打印出平均分是多少?

a = int(input("请输入第一科成绩: "))
b = int(input("请输入第二科成绩: "))
c = int(input("请输入第三科成绩: "))

# 方法1
# if a > b:
#     if a > c:
#         print("最高分是:", a)
#     else:
#         print("最高分是:", c)
# else:
#     if b > c:
#         print("最高分是:", b)
#     else:
#         print("最高分是:", c)

# 方法2
zhuida = a  # 先假设a最大
if b > zhuida:
    zhuida = b

if c > zhuida:
    zhuida = c

print("最高分是:", zhuida)
