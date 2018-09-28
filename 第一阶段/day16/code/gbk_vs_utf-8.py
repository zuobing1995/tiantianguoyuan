# gbk_vs_utf-8.py

f = open('linux_10hz.txt', 'rb')
b = f.read()  # 读到30字节
s = b.decode()
print('linux下写的十个字是:', s)
f.close()

f2 = open('windows_10hz.txt', 'rb')
b = f2.read()
f2.close()
s = b.decode('gbk')
print("Windows下写的十个汉字是:", s)  

