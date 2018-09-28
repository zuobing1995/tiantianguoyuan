# with.py


# 第一种方式用try-finally保证文件一定能够正常关闭
try:
    f = open("../../day19/day19.txt")
    try:
        for l in f:
            x = int('aaaa')  # 出现异常
            print(l)
    finally:
        f.close()
        print("文件已经关闭")
except OSError:
    print("打开文件失败")
