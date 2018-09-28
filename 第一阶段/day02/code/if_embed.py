# if_embed.py

# 示意if语句的嵌套
# 2. 输入一年中的月份(1~12) 输出这个月在哪个
#    季度,如果输入的是其它的数,则提示您输错了

m = int(input("请输入月份(1~12): "))
if 1 <= m <= 12:
    if m <= 3:
        print("春季")
    elif m <= 6:
        print("夏季")
    elif m <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您输错了")





















