# class_variable.py


total_count = 0  # 全局变量

class Human:

    def __init__(self, n):
        self.name = n
        global total_count
        total_count += 1
        print(n, '对象被创建')

    def __del__(self):
        print(self.name, '对象被销毁')
        global total_count
        total_count -= 1


L = []
L.append(Human('张飞'))
L.append(Human('关羽'))
print("当前人物个数是:", total_count)
del L[1]
print("当前人物个数是:", total_count)




