# 练习:
#   1. 写一个程序模拟现实电子字典
#      1) 输入一些单词和解释,将单词作为键,
#      将解释作用值,将这些数据输入到字典中,
#      当输入空单词时结束输入
#      2) 输入要查找的词,给出该单词的解释.
#       如果单词不存在则提示用户不存在该单词

d = {}  # 创建空典
while True:
    words = input('请输入单词: ')
    if words == '':
        break
    trans = input('请输入解释: ')
    d[words] = trans

while True:
    words = input("请输入要查找的单词: ")
    if words in d:
        print(words, "的解释是:", d[words])
    else:
        print(words, '这个单词在字典中不存在')



