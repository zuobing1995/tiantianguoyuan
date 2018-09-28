# super.py

# 此示例示意用super函数间接调用父类中覆盖版本的方法
class A:
    def work(self):
        print("A.work 被调用")

class B(A):
    '''B类继承自A类'''
    def work(self):
        print("B.work被调用!!!")

    def super_work(self):
        # 调用B类自己的方work方法怎么调用
        self.work()
        # 调用父类的work怎么调用
        super(B, self).work()
        super().work()  # 此种调用方式只能在实例方式内调用


b = B()
# b.work()  # B.work被调用!!!
# super(B, b).work()  # A.work 被调用
b.super_work()
# super().work()  # 出错


