# mynumer.py


# 此示例示意算术运算符的重载方法
class MyNumber:
    def __init__(self, v):
        self.data = v  # self.data 用来保存对象的数据

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self, other):
        '''此方法来用制定self + other的规则'''
        v = self.data + other.data
        return MyNumber(v)  # 用v创建一个新的对象返回给调用者

    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)


n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)
n3 = n1 + n2  # 等同于 n3 = n1.__add__(n2)
print(n3)  # MyNumber(300)
n4 = n3 - n2  # 等同于 n4 = n3.__sub__(n2)
print('n4 = ', n4)  # n4 =  MyNumber(100)

