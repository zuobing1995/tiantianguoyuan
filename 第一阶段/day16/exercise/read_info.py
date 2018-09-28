# 练习:
#   自己写一个文件 'info.txt' 内部存一些文字信息如下:
#     张三 20 100
#     李四 21 96
#     小王 20 98
#   注:
#     以上信息用空格作用分隔符分开
#   写程序将这些数据读取出来，并以如下格式打印出来:
#      张小 今年 20 岁,成绩是: 100
#      李四 今年 21 岁,成绩是: 96
#      小王 今年 20 岁,成绩是: 98


def read_info_txt():
    rl = []
    try:
        f = open("info.txt")
        L = f.readlines()  # ['张三 20 100\n', '李四 21 96\n', '小王 20 98\n']
        for line in L:
            s = line.strip()  # 去掉左右两侧的空白字符
            name, age, score = s.split()  # ['张三','20','100']
            age = int(age)  # 转为整数
            score = int(score)
            rl.append({'name': name,
                       'age': age,
                       'score': score})
        f.close()
        return rl  # 返回列表
    except OSError:
        print("读取文件失败!")


def print_info(L):
    for d in L:
        print(d['name'], '今年',
              d['age'], '岁,成绩是:',
              d['score'])


L = read_info_txt()
print_info(L)
