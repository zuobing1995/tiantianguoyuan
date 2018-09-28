# mynumber.py


# 此示例示意对象转字符串函数的重写方法
class MyNumber:
    def __init__(self, val):
        self.data = val  # 在每个对象内部都创建一个实例变量来绑定数据

    def __str__(self):
        # print("__str__方法被调用")
        return "自定义数字: %d" % self.data

    def __repr__(self):
        '''此方法返回来的字符串一定是能表示self对象的表达式字符串'''
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
print('str(n1) =', str(n1))  # 自定的数字:100
print('repr(n1) =', repr(n1))  # MyNumber(100)

n2 = MyNumber(200)
print(str(n2))
print(n2.__str__())
print(n2)  # 在print内部会将n2用str(x) 转为字符串再写到sys.stdout






