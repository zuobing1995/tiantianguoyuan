# slots.py


# 此示例示意类内__slots__列表的用法和作用
class Human:
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def info(self):
        print(self.name, '今年', self.age, '岁')


h1 = Human('小张', 8)
h1.info()  # 小张 今年 8 岁
# h1.Age = 9  # <<--此处会出错。__slots__列表限定不能有此属性
h1.info()  # 小张 今年 8 岁

