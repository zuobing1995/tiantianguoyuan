# len_overwrite.py


class MyList:
    '''这是一个自定义的列表类型,
    此类型的对象用data属性绑定的列表来存储数据'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        return len(self.data)

    def __abs__(self):
        L = [abs(x) for x in self.data]
        return MyList(L)


myl = MyList([1, -2, 3, -4])
print(myl)  # MyList([1, -2, 3, -4])
print(len(myl))   # 4
print(abs(myl))   # MyList([1, 2, 3, 4])

