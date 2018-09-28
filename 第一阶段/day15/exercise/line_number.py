# 练习:
#   写一个程序，读入任意行文字，当输入空行时结束输入
#   打印带有行号的输入结果
#     如:
#       请输入: abcde<回车>
#       请输入: hello<回车>
#       请输入: bye<回车>
#       请输入: <回车>
#     输出如下:
#       第1行: abcde
#       第2行: hello
#       第3行: bye

def get_lines():
    L = []
    while True:
        s = input("请输入: ")
        if not s:
            break
        L.append(s)
    return L


def print_lines(L):
    for t in enumerate(L, 1):
        print("第%d行: %s" % t)


L = get_lines()
print(L)
print_lines(L)

