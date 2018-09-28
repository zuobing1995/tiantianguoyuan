# exception.py


def f1():
    print("开始盖房子打地基...")
    # err = ValueError("打地基挖出古物，停止施工")
    # raise err
    print("地基完成")

def f2():
    print("开始盖房子地面以上部分....")
    err = ValueError("要建高压线...停止施工")
    raise err
    print("地面以上部分完工")


def f3():
    '''第一承包商开始找人盖房子'''
    f1()
    f2()


def build_house():
    '''第一承包商开始找人盖房子'''
    f3()


try:
    build_house()
except ValueError as err:
    print("出错:", err)

