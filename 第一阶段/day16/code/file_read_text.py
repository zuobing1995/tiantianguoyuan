# file_open.py


# 此示例示意文件 的打开及读取文本信息的操作

try:
    f = open("mynote.txt")  # 打开文件
    print("文件打开成功")
    # 读写文件
    s = f.readline()  # 读取一行  s='abcd\n'
    print('len(s)=', len(s), '内空是', s)
    s = f.readline()  # 再读取一行 s = '1234'
    print('len(s)=', len(s), '内空是', s)
    s = f.readline()  # 再读取第三行 s = '' 
    print('len(s)=', len(s), '内空是', s)

    # 关闭文件
    f.close()
    print("文件已关闭")
except OSError:
    print("文件打开失败")

