# write_text_to_file.py

#   1. 写程序，读入任意行文字，当输入空行时结束输入
#      先将这些读入的文字存入列表中， 然后再将列表
# 里的内容存入到'input.txt'文件中


def input_to_list():
    L = []
    while True:
        s = input("请输入: ")
        if not s:
            break
        L.append(s)
    return L


def list_to_file(lst, filename='input.txt'):
    '''将字符串的列表，保存在filename 文件中'''
    try:
        fw = open(filename, 'w')
        for s in lst:
            # 把s绑定的字符串写入到input.txt文件中
            fw.write(s)
            fw.write('\n')  # 写入换行符，用来区分行
        fw.close()
    except OSError:
        print("写入文件失败")


L = input_to_list()  # 读入数据
list_to_file(L)  # 写入到文件中


