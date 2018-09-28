# try_finally.py


def fry_egg():
    print("打开天燃气...")
    try:
        count = int(input("请输入鸡蛋个数: "))
        print("完成煎鸡蛋,共煎了%d个鸡蛋!" % count)
    finally:
        print('关闭天燃气')


try:
    fry_egg()
except:
    print("程序出现过异常，已转为正常状态")

print("程序正常退出")

