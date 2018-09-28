# 练习:
#   实现两个自定义列表的相加
#   class MyList:
#       def __init__(self, iterable=())
#            self.data = list(iterable)
#       .... 以下自己实现

#   L1 = MyList([1, 2, 3])
#   L2 = MyList([4, 5, 6])
#   L3 = L1 + L2
#   print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#   L4 = L2 + L1
#   print(L4)  # MyList([4, 5, 6, 1, 2, 3])
#   # 试想能否实现以下操作
#   L5 = L1 * 3
#   print(L5)  # MyList([1, 2, 3, 1, 2, 3, 1, 2, 3])


class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        '''rhs 为int类型, rhs.data 是不存在的'''
        return MyList(self.data * rhs)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])

# 试想能否实现以下操作
L5 = L1 * 3  # 等同于L5 = L1.__mul__(3)
print(L5)  # MyList([1, 2, 3, 1, 2, 3, 1, 2, 3])
