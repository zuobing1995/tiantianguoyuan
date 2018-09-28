# mylist3.py


# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        G = (-x for x in self.data)
        return MyList(G)

L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1  # <<---此处会有错误
print(L2)  # MyList([-1, 2, -3, 4, -5])
# L3 = +L1  




