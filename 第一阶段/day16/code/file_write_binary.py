# file_write_binary.py

 # 此示例示意二进制文件的写操作

try:
    fbw = open("mybinary.bin", 'wb')  # '二进制写操作'
    s = '你好'
    b = s.encode('utf-8')  # 转为字节串
    fbw.write(b)
    ba = bytearray(range(256))
    fbw.write(ba)
    fbw.close()
    print("文件写入成功")
except OSError:
    print("打开写文件失败")

