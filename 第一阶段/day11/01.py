# map(fun,iters) 

# for i in map(lambda x:x**2,[1,2,3,4]):
#     print(i)

# filter(fun,iters):返回可迭代对象 fun筛选iters 内的数据，
# 对每个数据进行bool求值,为true 保存

# def fun(x):
#     return x%2==0
# for i in filter(fun,range(1,10)):
#     print(i)

# sorted:将原可迭代对象排序，返回排序后的列表
# 排序规则根据：key =函数返回的结果
# l=['tom','join','zz']
# def fun(s):
#     return s[::]
# l1=sorted(l,key=fun,reverse=False)
# print(l1)


closure:闭包

1 是嵌套函数
2 返回的是一个函数
3 内部嵌套函数调用了外部函数的变量



def fun(x,y):

    def fun1(y):
        return x+y #调用了外部变量x，本该执行完毕销毁的x 
        # 和函数fun1和外部执行环境捆绑在一起
    return fun1
fun(100,200)
