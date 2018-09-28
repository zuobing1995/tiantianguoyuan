# 3. 输入三行文字,让这三行文字在一个方框内居中显示
#   如输入(不要输入中文)
#   hello!
#   I'm studing python!
#   I like python
# 打印如下:
#  +---------------------+
#  |       hello!        |
#  | I'm studing python! |
#  |    I like python    |
#  +---------------------+

a = input("请输入: ")
b = input("请输入: ")
c = input("请输入: ")

max_len = max(len(a), len(b), len(c))
first_line = '+' + '-' * (max_len + 2) + '+'
print(first_line)  # 打印第一行

print('|', a.center(max_len), '|')
print('|', b.center(max_len), '|')
print('|', c.center(max_len), '|')


print(first_line)  # 打印最后一行　


