# mynumber.py


# 此示例示意数值转换函数的重写
class MyNumber:
    def __init__(self, val):
        self.data = val

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __int__(self):
        '''重写int(obj) 函数'''
        return int(self.data)

    def __float__(self):
        return float(self.data)


n1 = MyNumber(100)
n = int(n1)  # 出错
print(n)

f = float(n1)
print(f)

c = complex(n1)  # 当没有n1.__complex__() 时会调用n1.__float__() + 0j
print(c)





