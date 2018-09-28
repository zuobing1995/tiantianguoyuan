# student.py


'''模块用于定义一个学生类,此类用于
生成学生对象,来存储学生相关的信息'''
class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def get_info(self):
        '''此方法用来返回学生信息的元组'''
        return (self.name, self.age, self.score)

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def save(self, file):
        '''学生拿到文件后,自己来向文件里写东西'''
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')






