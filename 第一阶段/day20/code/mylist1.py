# mylist1.py


# 此示例示意反向算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        '''rhs 为int类型, rhs.data 是不存在的'''
        print("__mul__ 被调用")
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用")
        return MyList(self.data * lhs)


L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])

L3 = 3 * L1
print(L3)

