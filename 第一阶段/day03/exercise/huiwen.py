# 2. 输入任意一个字符串,判断这个字符串是否是回文
#   回文示例:
#     上海自来水来自海上
#     ABCCBA
#     12321
#   回文是指中心对称的文字

s = input('请输入一段字符串: ')

if s == s[::-1]:
    print(s, '是回文')
else:
    print(s, '不是回文')


