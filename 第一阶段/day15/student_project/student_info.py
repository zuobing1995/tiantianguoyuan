

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


def print_info_by_score_desc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)


def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score)
    output_student(L2)


def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(L2)


def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d['age'])
    output_student(L2)




