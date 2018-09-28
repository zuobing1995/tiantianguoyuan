# print.py

print(1, 2, 3, 4)  # 等同于print(1, 2, 3, 4, sep=' ')
print(1, 2, 3, 4, sep='#')
print(1, 2, 3, 4, sep='')  # 1234
print("hello world", sep='####')  # 分隔符无效

print(1, 2, 3, 4, end='\n')
print(5, 6, 7, 8, end='$$$$$$$')
print("abcd", end='\n\n\n')


