# 练习:
#   写一个程序，输入你的出生日期
#     1) 算出你已经出生了多少天?
#     2) 算出你出生那天是星期几?

import time

year = int(input("请输入出生的年: "))
month = int(input("请输入出生的月: "))
day = int(input("请输入出生的年日: "))

# 出生的秒数(计算机元年开始)
birth_second = time.mktime((year,
                           month,
                           day,
                           0,
                           0,
                           0,
                           0, 0, 0))


cur_second = time.time()  # 当前的秒数(计算机元年开始)
life_second = cur_second - birth_second
days = life_second // 60 // 60 // 24  #　天数
print("您共出生了%d天" % days)


# 得到出生那天的时间元组
t = time.localtime(birth_second)
week = {
    0: "星期一",
    1: "星期二",
    2: "星期三",
    3: "星期四",
    4: "星期五",
    5: "星期六",
    6: "星期日"
}
print("出生那天是:", week[t[6]])


