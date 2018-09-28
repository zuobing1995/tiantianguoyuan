# property.py



class Student:
    def __init__(self, s):
        self.__score = s

    def setScore(self, s):
        '''此方法用设置值加以限制以保证数据的准确性
        setter是用来数据的
        '''
        if 0 <= s <= 100:
            self.__score = s

    def getScore(self):
        '''getter 只用来获取数据'''
        return self.__score


s = Student(50)
s.setScore(100)

# s.score = 100
# print(s.score)
# s.score = 10000
# print(s.score)