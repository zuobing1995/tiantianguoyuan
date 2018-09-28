# enclosure.py


# 此示例示意用私有属性和私有方法来实现封装
class A:
    def __init__(self):
        self.__p1 = 100  # <<--- __p1为私有属性
        # self.__p2__ = 200  # 这人不是私有属性

    def show_info(self):
        print(self.__p1)  #此对象的实例方法可以访问和修改私有属性
        self.__m()  # 调用私有方法

    def __m(self):
        print("A类对象的__m方法被调用")

a = A()
a.show_info()  # 100
# a.__m()  # 出错, 除A类的实例方法外,不能调用a对象的私有方法
# print(a.__p1)  # 不允许访问私有属性
# print(a.__p2__)






