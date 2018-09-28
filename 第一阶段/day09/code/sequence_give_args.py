# sequence_give_args.py


# 此示例示意序列传参
def myfun(a, b, c):
    '这是一个函数传参的示例'
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)


s1 = [11, 22, 33]
s2 = (44, 55, 66)
s3 = "ABC"
myfun(*s1)  # 等同于　myfun(s1[0], s1[1], s1[2])  # 11 -->a, 22 --> b, 33 --> c
myfun(*s2)  # 等同于　myfun(s2[0], s2[1], s2[2])
myfun(*s3)  # 等同于　myfun(s3[0], s3[1], s3[2])

