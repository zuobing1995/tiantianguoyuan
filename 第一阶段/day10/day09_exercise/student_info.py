# 2. 实现带有界面的学生信息管理系统
#   操作界面:
#     +-------------------------+
#     | 1)  添加学生信息          |
#     | 2)  显示学生信息          |
#     | 3)  删除学生信息          |
#     | 4)  修改学生信息          |
#     | q)  退出                 |
#     +-------------------------+
#     请选择: 1

#   修改之前学生信息管理程序,学生信息依旧为:
#        姓名,年龄,成绩
#   要求: 每个功能写一个函数与之相对应

# 示意:
#   def main():
#       L = []
#       while True:
#           # 此处先显示菜单
#           s = input("请选择: ")
#           if s == 'q':
#               break
#           elif s == '1':
#               L += input_student()
#           elif s == '2':
#               output_student(L)
#           ...
#   main()


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

def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count

    
def output_student(L):
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']
        s = d['score']
        chinese_cnt = get_chinese_char_count(n)
        print('|%s|%s|%s|' % (n.center(15-chinese_cnt),
                              str(a).center(10),
                              str(s).center(10)
                              )
              )

    # print("|    tarena     |    20    |     99   |")
    # print("|     name2     |    30    |     88   |")
    print("+---------------+----------+----------+")


def del_student(L):
    n = input('请输入要删除的学生的姓名: ')
    print("正在删除....", n)


def modify_student_score(L):
    print("正在修改学生成绩....")


def show_menu():
    print("+---------------------------+")
    print("| 1)  添加学生信息          |")
    print("| 2)  显示学生信息          |")
    print("| 3)  删除学生信息          |")
    print("| 4)  修改学生成绩          |")
    print("| q)  退出                 |")
    print("+---------------------------+")


def main():
    L = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            break
        elif s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_student(L)
        elif s == '4':
            modify_student_score(L)


main()


