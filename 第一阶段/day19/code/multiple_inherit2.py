# multiple_inherit2.py


# 小张写了一个类A:
class A:
    pass
    # def m(self):
    #     print("A.m() 被调用")

# 小李写了一个类B:
class B:
    def m(self):
        print("B.m() 被调用")

# 小王感觉小张和小李写的两个类自己都可以用
class AB(A, B):
    pass
    # def m(self):
    #     print("AB.m() 被调用")

ab = AB()
ab.m()  # 请问调用谁? 为什么?
