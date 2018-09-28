# seek.py


# 此示例示意seek方法的用法
f = open('20.txt', 'rb')  # 二进制方式打开
b = f.read(3)  # 读了三个字节
print(b)

# f.seek(5, 0)  # 代表从文件头向后移动5个字节
# f.seek(2, 1)  # 代表从当前位置向后移动2个字节
f.seek(-15, 2)  # 代表从文件尾向前移动15个字节

b = f.read(5)
print(b)  # b'ABCDE'

f.close()