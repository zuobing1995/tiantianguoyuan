# pass.py

# 此示例示意pass语句的用法
# 输入一个学生的成绩.如果成绩不在0~100之间,
# 则提示错误

score = int(input("请输入学生成绩: "))
if 0 <= score <= 100:
    pass
else:
    print("不合法的成绩!")

