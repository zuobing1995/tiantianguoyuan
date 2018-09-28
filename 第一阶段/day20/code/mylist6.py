# mylist3.py


# 此示例示意切片取值操作
class MyList:
    def __init__(self, iterable=()):
        self.__data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.__data

    def __getitem__(self, i):
        print('i的值是:', i)
        if type(i) is int:
            print("用户正在用索引取值")
        elif type(i) is slice:
            print("用户正在用切片取值")
            print("切片的起点是:", i.start)
            print("切片的终点是:", i.stop)
            print("切片的步长是:", i.step)
        elif type(i) is str:
            print("用户正在用字符串进行索引操作")
            # raise KeyError
            return "你想用字符串做什么？"

        return self.__data[i]  # 返回data绑定列表中的第i个元素


L1 = MyList([1, -2, 3, -4, 5])
print(L1[::2])  # 切片取值
print(L1["ABC"])
