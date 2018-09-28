# flush.py

import time

f = open('myflush.txt', 'w')

f.write('aaaaaaaa')
f.flush()  # 强制将缓冲区的内容写到磁盘上

s = input("请输入回车键继续: ")

f.close()

