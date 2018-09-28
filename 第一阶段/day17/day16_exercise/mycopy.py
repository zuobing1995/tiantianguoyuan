# 3. 写程序，实现复制文件功能
#   要求:
#     1) 要考虑关闭文件问题
#     2) 要考虑超大文件复制问题
#     3) 要能复制二进制文件(如:/usr/bin/python3 等文件)

def mycopy(src_filename, dst_filename):  # 源文件名和目标文件名
    try:
        fr = open(src_filename, 'rb')
        try:
            try:
                fw = open(dst_filename, 'wb')
                try:
                    while True:
                        b = fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print("打开目标文件失败")
        finally:
            fr.close()
    except OSError:
        print("打开源文件失败")



src = input("请输入源文件名:")
dst = input("请输入目标文件名:")
mycopy(src, dst)
