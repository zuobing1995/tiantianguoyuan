# flush.py

import time

f = open('myflush.txt', 'w')

while True:
    f.write('aaaaaaaa' * 100)
    time.sleep(1)
    print("写入一次...")

s = input("请输入回车键继续: ")

f.close()

