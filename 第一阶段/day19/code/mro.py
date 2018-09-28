# mro.py


class A:
    def go(self):
        print("A")

class B(A):
    def go(self):
        print("B")
        super().go()  # C

class C(A):
    def go(self):
        print("C")

class D(B, C):
    def go(self):
        print("D")
        super().go()  # 调用谁?

d = D()
d.go()