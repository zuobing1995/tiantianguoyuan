# class_variable.py


# 此示例示意用类变量来记录Human对象的个数
class Human:
    total_count = 0  # 类变量，用来记录Human对象的个数

    def __init__(self, n):
        self.name = n
        self.__class__.total_count += 1
        print(n, '对象被创建')

    def __del__(self):
        print(self.name, '对象被销毁')
        self.__class__.total_count -= 1


L = []
L.append(Human('张飞'))
L.append(Human('关羽'))
print("当前人物个数是:", Human.total_count)
del L[1]
print("当前人物个数是:", Human.total_count)




