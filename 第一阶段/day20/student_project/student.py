# student.py


'''模块用于定义一个学生类,此类用于
生成学生对象,来存储学生相关的信息'''
class Student:
    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s

    def get_info(self):
        '''此方法用来返回学生信息的元组'''
        return (self.__name, self.__age, self.__score)

    def get_score(self):
        return self.__score

    def get_age(self):
        return self.__age

    def save(self, file):
        '''学生拿到文件后,自己来向文件里写东西'''
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')






