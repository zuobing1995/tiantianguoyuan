# property.py


import math

import mymod


class Student:
    def __init__(self, s):
        self.__score = s

    @property
    def score(self):
        '''getter 只用来获取数据'''
        print("getter被调用")
        return self.__score

    @score.setter
    def score(self, s):
        '''此方法用设置值加以限制以保证数据的准确性
        setter是用来数据的
        '''

        print("setter被调用")
        if 0 <= s <= 100:
            self.__score = s


s = Student(50)
# s.setScore(100)

score = s.score  # 访问特性属性score 实质是调用原s.score()
print('成绩是:', score)
s.score = 100
print(s.score)  # 100
s.score = 10000
print(s.score)  # 100
