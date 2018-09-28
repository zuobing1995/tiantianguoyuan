# try_finally_test.py

x = 100
y = 200
try:
    save_x = x
    save_y = y
    try:
        x = int(input("请输入x:"))
        y = int(input("请输入y:"))
        # 用x, y当前值来调有和打印,打印完毕后，x,y依旧恢复原有数据
        print("x=", x, "y =", y)
    finally:
        x = save_x
        y = save_y
except:
    pass

print("原始数据　依旧为 x=", x, "y =", y)




