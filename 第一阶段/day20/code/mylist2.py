# mylist1.py


# 此示例示意反向算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        print('__add__ 被调用')
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        '''rhs 为int类型, rhs.data 是不存在的'''
        print("__mul__ 被调用")
        return MyList(self.data * rhs)

    # def __iadd__(self, rhs):
    #     print("__iadd__ 方法被调用")
    #     self.data += rhs.data  # 请问这是在做什么?
    #     return self

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])

print(id(L1))
L1 += L2  # L1 = L1 + L2  # L1.__iadd__(L2)
print(id(L1))
print(L1)

# L2 *= 3  # L2 = L2 * 3
# print(L2)


