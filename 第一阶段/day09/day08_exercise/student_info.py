# 5.  改写之前的学生信息管理程序，将其改为两个函数：
#   def input_student():
#         ...
#   def output_student(L):
#       ....
#   input_student用于从键盘读取学生数据，形成列表并返回列表
#   output_student(L) 用于将传和的列表L 打印成为表格
# 测试代码：
#   L = input_student()
#   print(L)
#   output_student(L)  # 打印表格


def input_student():
    L = []  # 创建一个新的列表，用此列表准备保存学生信息
    # 录入学生信息
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        s = int(input('请输入成绩: '))
        # 创建一个新的字典，把学生的信息存入字典中
        d = {}  # 每一次都重新创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)
    return L

    
def output_student(L):
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']
        s = d['score']
        print('|%s|%s|%s|' % (n.center(15),
                              str(a).center(10),
                              str(s).center(10)
                              )
              )

    # print("|    tarena     |    20    |     99   |")
    # print("|     name2     |    30    |     88   |")
    print("+---------------+----------+----------+")


L = input_student()
print(L)
output_student(L)  # 打印表格


