# mynumber.py


# 此示例示意对象转字符串函数的重写方法
class MyNumber:
    def __init__(self, val):
        self.data = val

    # def __str__(self):
    #     # print("__str__方法被调用")
    #     return "自定义数字: %d" % self.data

    def __repr__(self):
        '''此方法返回来的字符串一定是能表示self对象的表达式字符串'''
        return "MyNumber(%d)" % self.data


n1 = MyNumber(100)
print(n1)  # print(str(n1))





