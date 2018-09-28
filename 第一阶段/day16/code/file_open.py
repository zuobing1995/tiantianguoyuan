# file_open.py


# 此示例示意文件 的打开和关闭

try:
    # f = open("mynote.txt")  # 打开文件
    f = open('/home/tarena/aid1807/pbase/day16/code/mynote.txt')
    print("文件打开成功")

    # 读写文件

    # 关闭文件
    f.close()
    print("文件已关闭")
except OSError:
    print("文件打开失败")

