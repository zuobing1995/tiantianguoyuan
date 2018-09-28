# myiterator.py


# 此示例示意将自定义的类MyList创建的对象制作成为可迭代对象

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __iter__(self):
        '''此方法用于返回一个能访问self对象的迭代器'''
        print("__iter__被调用")
        return MyListIterator(self.data)  # 创建迭代器并返回


class MyListIterator:
    '''此类用来描述能够访问MyList类型的对象的迭代器'''
    def __init__(self, lst):
        self.data_lst = lst
        self.cur_index = 0   # 迭代器访问的起始位置

    def __next__(self):
        '''此方法用来实现迭代器协议'''
        print('__next__方法被调用')
        if self.cur_index >= len(self.data_lst):
            raise StopIteration

        r = self.data_lst[self.cur_index]
        self.cur_index += 1
        return r


myl = MyList([2, 3, 5, 7])
it = iter(myl)  # 等同于调用 it = myl.__iter__()
print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # 5
# print(next(it))  # 7
# print(next(it))  # StopIteration

for x in myl:
    print(x)

L = [x**2 for x in myl]
print(L)

