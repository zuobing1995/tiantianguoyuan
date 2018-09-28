# with.py


# 第二种方式用with语句保证文件一定能够正常关闭
try:
    with open("../../day19/day19.txt") as f:
        for l in f:
            x = int('aaaa')  # 当进入异常流程时,打开的文件也能被关闭
            print(l)

    # f = open("../../day19/day19.txt")
    # try:
    #     for l in f:
    #         x = int('aaaa')  # 出现异常
    #         print(l)
    # finally:
    #     f.close()
    #     print("文件已经关闭")
except OSError:
    print("打开文件失败")
