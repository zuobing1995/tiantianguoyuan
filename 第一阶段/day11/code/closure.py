# closure.py


# 写一个函数来创建 x的y次方的函数
def make_power(y):
    def fn(x):
        return x ** y
    return fn


pow2 = make_power(2)
print('5的方平是:', pow2(5))


def pow3(x):
    return x ** 3

pow3 = make_power(3)
print('6的三次方是:', pow3(6))
print('5的三次方是:', pow3(5))

pow10 = make_power(10)
print("2的十次方法:", pow10(2))








