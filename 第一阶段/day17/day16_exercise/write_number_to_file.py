# write_number_to_file.py

# 1. 写程序，让用户输入一系列整数，当输入小于零的数时结束输入
#   1) 将这些数字存于列表中
#   2) 将列表中的数字写入到文件numbers.txt中
#   (提示:需要将整数转为字符串或字节串才能存入文件中)

L = []
while True:
    n = int(input("请输入大于0的整数: "))
    if n < 0:
        break
    L.append(n)

print(L)
try:
    f = open('numbers.txt', 'w')  # 文本文件方式打开
    for n in L:
        f.write(str(n))  # 出错
        f.write('\n')
    f.close()
except OSError:
    print("文件打开失败")
