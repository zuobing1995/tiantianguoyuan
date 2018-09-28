# bool.py


class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        print("__len__方法被调用")
        return len(self.data)

    def __bool__(self):
        print("__bool__方法被调用")
        for x in self.data:
            if x:
                return True
        return False
        # return any(self.data)


myl = MyList([False, 0, 0.5])
print(bool(myl))
if myl:
    print(myl, '的布尔值为True')
else:
    print(myl, '的布尔值为False')


