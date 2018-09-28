

from student import Student

def input_student():
    L = []  # 创建一个新的列表，用此列表准备保存学生信息
    # 录入学生信息
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input('请输入成绩: '))
        except:
            print("您的输入有错，请新输入...")
            continue
        L.append(Student(n, a, s))
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
        n, a, s = d.get_info()
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


def print_info_by_score_desc(L):
    def get_score(d):
        return d.get_score()

    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)


def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d.get_score()

    L2 = sorted(L, key=get_score)
    output_student(L2)


def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d.get_age(), reverse=True)
    output_student(L2)


def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d.get_age())
    output_student(L2)


def save_to_file(L, filename='si.txt'):
    try:
        f = open(filename, 'w')
        for stu in L:
            # 第一,把学生的信息拿到当前来由'我'来往文件里写
            # f.write(stu.name)...
            stu.save(f)  # 第二,把文件 交给学生,由学来写
        f.close()
        print("保存成功")
    except OSError:
        print("写文件失败")


def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for line in f:
            n, a, s = line.strip().split(',')
            a = int(a)
            s = int(s)  # 转为整数

            L.append(Student(n, a, s))

        f.close()
    except OSError:
        print("读取文件失败")

    return L



