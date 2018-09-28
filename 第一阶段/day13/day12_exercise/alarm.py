# 2. 编写一个闹钟程序，启动时设置定时间, 到时间后打印一句:
#     "时间到",然后程序退出

import time

def alarm(h, m):
    while True:
        # 得到当前时间
        t = time.localtime()
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        # if h == t[3] and m == t[4]:
        if (h, m) == t[3:5]:
            print("\n时间到")
            break
        time.sleep(1)


hour = int(input("请输入定时小时: "))
minute = int(input("请输入定时分钟: "))
alarm(hour, minute)

