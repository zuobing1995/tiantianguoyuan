# mymod.py

'''这是一个自定义模块mymod的文档字符串

此模块有两个函数和两个数据...
此处省略100字
'''

# 此示例示意自义模块
def myfac(n):
    print("正在计算%d的阶乘...." % n)


def mysum(n):
    print("正在计算1+2+3+....+", n, '的和....')


name1 = "audi"
name2 = 'Tesla'

print('mymod模块被加载!')

print("我的模块名是:", __name__)

if __name__ == '__main__':
    print("我正在以主模块方式运行")
    mysum(10000)
