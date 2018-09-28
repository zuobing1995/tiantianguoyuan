# file_read_binary.py


# 此示例示意用二进制方式读取文件内容

try:
    fr = open('mynote.txt', 'rb')  # 二进制读方式打开

    b = fr.read()  # b = b'abcd\n1234' 返回字节串
    print(b)

    fr.close()

except OSError:
    print("打开二进制文件失败")

