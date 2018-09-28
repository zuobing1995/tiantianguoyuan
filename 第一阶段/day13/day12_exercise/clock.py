
# 1. 写一个程序，打印电子时间:
#     格式为:
#       HH:MM:SS
#     每过一秒钟刷新一次

import time

while True:
    t = time.localtime()  # 得到当前时间的元组
    # print("%02d:%02d:%02d" % (t[3], t[4], t[5]))
    print("%02d:%02d:%02d" % t[3:6], end='\r')
    time.sleep(1)


