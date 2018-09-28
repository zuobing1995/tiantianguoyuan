# def2.py


# 此示例示意定义带有参数的函数，及调用
def mymax(a, b):
    if a > b:
        print("最大值是", a)
    else:
        print("最大值是", b)


mymax(100, 200)  # 200 # 传参调用
mymax(50, 30)  # 50
mymax("ABC", "123")
# mymax(1, 2, 3, 4)  # 出错
