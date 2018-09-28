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
    L = []

    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    @classmethod
    def add_student(cls):
        cls.L.append(Student("小张", 20, 100))
        cls.L.append(Student("小李", 18, 80))
        cls.L.append(Student("小赵", 19, 90))

    @classmethod
    def del_student(cls):
        del cls.L[0]

    @classmethod
    def get_student_count(cls):
        return len(cls.L)

    @classmethod
    def get_avg_score(cls):
        return sum(map(lambda obj: obj.score, cls.L)) / len(cls.L)

    @classmethod
    def get_avg_age(cls):
        return sum(map(lambda obj: obj.age, cls.L)) / len(cls.L)


Student.add_student()
print("学生个数是: ", Student.get_student_count())
print("学生的平均成绩是: ", Student.get_avg_score())
print("学生的平均年龄是: ", Student.get_avg_age())
Student.del_student()
print("学生个数是: ", Student.get_student_count())
print("学生的平均成绩是: ", Student.get_avg_score())
print("学生的平均年龄是: ", Student.get_avg_age())







