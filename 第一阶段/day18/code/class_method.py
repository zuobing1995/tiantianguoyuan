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
A.set_v(100)

print("A.v =", A.get_v())  # 100
print(A.v)  # 100
