# file_write_text.py


# f = open("newfile")
# 如果不写第二个参数默认是:  f = open('newfile', 'rt')

try:
    # f = open("/root/newfile.txt", 'wt')  # 失败抛出异常错误通知
    f = open("newfile.txt", 'w')
    # f = open("newfile.txt", 'x')  # 如果原文件存在，则报错
    # f = open("newfile.txt", 'a')  # 如果原文件存在，则报错
    print("打开成功")

    # 在此处进行写文件操作
    f.write("hello")
    f.write("world")
    f.writelines(['123456\n', 'abcdef\n'])

    f.close()
    print("关闭文件成功")
except OSError:
    print("创建文件失败")

