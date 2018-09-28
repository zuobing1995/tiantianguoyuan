# 思考:
#   list类里只有append向末尾加一个元素的方法，但没有向列表头部添加元素的方法。
#   试想能否为列表在不改变原有功能的基础上添加一个insert_head(x)方法，此方法能在列表的前部添加元素
#     class MyList(list):
#         def insert_head(self, x):
#             ....
#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]


class MyList(list):
    def insert_head(self, x):
        # self.insert(0, x)
        self[0:0] = [x]


myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]
myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]
myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]

    