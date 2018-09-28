# 4. 用程序生成如下字符串:
#    1) "ABCDEFG..... XYZ"
#    2) "AaBbCcDdEe......XxYyZz"
#   提示(可以使用 ord 和 chr函数)
#     参考 ascii编码

s = ''  # 先创建一个空字符串
# for code in range(65, 65 + 26):
for code in range(ord('A'), ord('Z') + 1):
    s += chr(code)  # 用编码值生成字符串,追加到s末尾
print(s)

s2 = ''
for code in range(65, 65 + 26):
    s2 += chr(code)  # 追加一个大写字母
    s2 += chr(code + 32)  # 追加一个对应的小写字母
print(s2)

