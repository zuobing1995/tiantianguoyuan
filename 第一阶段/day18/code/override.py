# override.py


# 此示例示意覆盖的含义及用法
class A:
    def work(self):
        print("A.work 被调用")


class B(A):
    '''B类继承自A类'''
    def work(self):
        print("B.work被调用!!!")


b = B()
b.work()  # B.work被调用!!!

a = A()
a.work()  # A.work 被调用
