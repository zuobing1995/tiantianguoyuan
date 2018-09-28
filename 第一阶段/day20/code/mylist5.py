# mylist3.py


# 此示例示意 in / not in 运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.__data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.__data

    def __getitem__(self, i):
        '索引取值,i绑定[]内的元素'
        print('i的值是:', i)
        return self.__data[i]  # 返回data绑定列表中的第i个元素

    def __setitem__(self, i, v):
        '''此方法可以让自定义的列表支持索引赋值操作'''
        print("__setitem__被调用, i=", i, 'v=', v)
        self.__data[i] = v

    def __delitem__(self, i):
        self.__data.pop(i)  # del self.__data[i]

L1 = MyList([1, -2, 3, -4, 5])
x = L1[3]  # 能否用索引来访问自定义的MyList类型的对象呢
print(x)

L1[3] = 400  # 索引赋值
print(L1)

del L1[3]
print(L1)  # MyList([1, -2, 3, 5])

# 思考如下语句能执行吗?
print(L1[::2])  # 切片取值
