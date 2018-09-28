# class_method.py

class A:
    v = 0  # 类变量(类属性)

    @classmethod
    def get_v(cls):
        return cls.v  # 用cls 访问类变量v

    @classmethod
    def set_v(cls, a):
        cls.v = a

print('A.v = ', A.get_v())  # 调用类方法得到类变量的值

a = A()  # a绑定A类型的一个实例对象
print(a.get_v())  # 此类的实例也可以调用该类方法
a.set_v(999)
print('A.v = ', A.get_v())  # 999
