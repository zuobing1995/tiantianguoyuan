# seek.py


# 此示例示意tell方法的用法
f = open('20.txt', 'rb')  # 二进制方式打开
b = f.read(3)  # 读了三个字节
print(b)
# 请问当前读写位置在哪儿呢？
pos = f.tell()  # 返回读写位置
print("当前的读写位置是: ", pos)  # 3
b2 = f.read(1)
print("再读一个字节后的读写位置是:", f.tell())  # 4

f.close()