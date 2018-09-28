# def myfun(a,b,c):
#     print9('a的值',a)
#     print9('b的值',b)
#     print9('c的值',c)
# myfun(1,2,3)
# myfun(3,2,1)

# def myfun(a,b,c,d=4):  #在形参中给出默认参数,当实参没有传递来参数时,默认形参中的
#     print('a的值',a)
#     print('b的值',b)
#     print('c的值',c)
#     print('d的值',d)
# a=[1,2,3]
# myfun(*a)
# myfun(3,2,1)
def myfun(a,b,c):
    print('a的值',a)
    print('b的值',b)
    print('c的值',c)
z={'c':100,'b':200,'a':300}
myfun(**z)