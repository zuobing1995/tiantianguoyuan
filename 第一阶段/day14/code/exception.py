# exception.py


def f1():
    print("开始盖房子打地基...")
    # err = ValueError("打地基挖出古物，停止施工")
    # return err
    print("地基完成")

def f2():
    print("开始盖房子地面以上部分....")
    err = ValueError("要建高压线...停止施工")
    return err
    print("地面以上部分完工")


def f3():
    '''第一承包商开始找人盖房子'''
    r = f1()
    if r is not None:
        return r
    r = f2()
    if r is not None:
        return r


def build_house():
    '''第一承包商开始找人盖房子'''
    r = f3()
    if r is not None:
        return r

r = build_house()
if r is not None:
    print("出错:", r)
