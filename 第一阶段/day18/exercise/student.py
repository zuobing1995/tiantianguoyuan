# 练习：
#    用类来描述一个学生的信息，(可以修改之前写的Student类)
#     class Stdent:
#         ...此处自己实现
#     学生信息有:
#         姓名，年龄，成绩
#     将这些学生对象存于列表中，可以任意添加和删除学生
#       1) 打印出学生的个数
#       2) 打印出学生的平均成绩
#       3) 打印出学生的平均年龄
#       （建议用类内的列表来存储学生的信息)
    

class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

L = []

def add_student(L):
    L.append(Student("小张", 20, 100))
    L.append(Student("小李", 18, 80))
    L.append(Student("小赵", 19, 90))

def del_student(L):
    del L[0]

def get_student_count(L):
    return len(L)

def get_avg_score(L):
    return sum(map(lambda obj: obj.score, L)) / len(L)

def get_avg_age(L):
    return sum(map(lambda obj: obj.age, L)) / len(L)


add_student(L)
print("学生个数是: ", get_student_count(L))
print("学生的平均成绩是: ", get_avg_score(L))
print("学生的平均年龄是: ", get_avg_age(L))
del_student(L)
print("学生个数是: ", get_student_count(L))
print("学生的平均成绩是: ", get_avg_score(L))
print("学生的平均年龄是: ", get_avg_age(L))







