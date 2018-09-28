# mylist3.py


# 此示例示意 in / not in 运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __contains__(self, e):
        # print("+++++++++")
        return True if e in self.data else False
        # return e in self.data


L1 = MyList([1, -2, 3, -4, 5])

if 2 in L1:  # 等同于 if L1.__contains__(2):
    print("2在L1内")
else:
    print('2不在L1内')

if 4 not in L1:  # 等同于 if not L1.__contains__(4)
    print("4不在L1内")
else:
    print("4在L1内")

