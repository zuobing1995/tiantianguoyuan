# inherit.py


# 此示例示意单继承的定义方法和用法
class Human:
    def say(self, what):
        print("说:", what)

    def walk(self, distance):
        print("走了", distance, '公里')


class Student(Human):
    def study(self, subject):
        print("正在学习", subject)


class Teacher(Human):
    def teach(self, subject):
        print("正在教", subject)


h1 = Human()
h1.say('今天天气真好')
h1.walk(5)


s1 = Student()
s1.walk(4)
s1.say('感觉有点累')
s1.study('Python')


t1 = Teacher()
t1.teach("面向对象")
t1.walk(6)
t1.say('太累了，今天晚吃啥')


