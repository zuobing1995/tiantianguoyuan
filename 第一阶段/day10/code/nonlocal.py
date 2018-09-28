# nonlocal.py


v = 100
def f1():
    v = 200
    print("f1.v=", v)

    def f2():
        nonlocal v
        v = 300
        print("f2.v=", v)
    f2()
    print("调用f2()后的f1.v = ", v)
f1()
print("全局的v=", v)







