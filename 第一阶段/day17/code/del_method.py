# del_method.py

# 此示例示意析构方法的使用
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车对象", info, '被创建')

    def __del__(self):
        print("汽车对象", self.info, '被销毁')


c1 = Car("BYD E6")
# c1 = None  # 改变变量的绑定关系可以释放 BYD E6对象
del c1  # 删除变量，释放对象
L = []
L.append(Car("汽车1"))
L.append(Car("汽车2"))
L.append(Car("汽车3"))
del L  # 释放列表
input("请输入回车键继续执行程序: ")
print("程序退出")


