# read_text_from_file.py

def read_from_file(filename='input.txt'):
    L = []
    try:
        fr = open(filename, 'rt')
        for line in fr:
            s = line.rstrip()  # 去掉最右侧的空白字符
            L.append(s)
        fr.close()
        print("读取文件成功")
    except OSError:
        print("打开读文件失败!!!")
    return L


def print_text(lst):
    for line_number, s in enumerate(lst, 1):
        print(line_number, ":", s)


if __name__ == '__main__':
    print_text(read_from_file())


