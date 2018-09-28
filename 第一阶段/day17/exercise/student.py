# 练习:
#   1. 写一个Student类,此类创建的对象有三个属性:
#       姓名，年龄，成绩
#     1) 用初始化方法为该类添加上述三个属性
#     2) 添加set_score()　方法能为对象修改学生成绩
#     3) 添加show_info()　方法,打印学生信息
#     如:
#       class Student:
#           def __init__(.....):
#               ....
#           def set_score(self, score):
#                ....
#           def show_info(self):
#               ....
#       L = []
#       L.append(Student('小张', 20, 100))
#       L.append(Student('小李', 18, 95))
#       L.append(Student('小魏', 8))
#       L[2].set_score(70)
#       for obj in L:
#           obj.show_info()  # 小张　20　岁， 成绩: 100  ....


class Student:
    def __init__(self, n, a, s=0):
        self.name, self.age, self.score = n, a, s

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score

    def show_info(self):
        print(self.name, self.age, '岁，成绩:', self.score)


L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 95))
L.append(Student('小魏', 8))
L[2].set_score(70)
for obj in L:
    obj.show_info()  # 小张　20　岁， 成绩: 100  ....
