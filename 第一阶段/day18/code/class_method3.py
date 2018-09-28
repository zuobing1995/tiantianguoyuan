# class_method.py


# 类方法不能访问该类对象的实例属性
class A:
    v = 0  # 类变量(类属性)

    @classmethod
    def set_v(cls, a):
        '''此类方法不能访问 a.color 属性'''
        cls.v = a


a = A()  # a绑定A类型的一个实例对象
a.color = '#FF0000'
a.set_v(100)


