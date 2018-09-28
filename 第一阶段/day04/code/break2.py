# break.py

i = 1
while i <= 6:
    print('循环开始时:', i)
    if i == 3:
        break
    print('循环结束时:', i)
    i += 1
else:
    print('这是while语句的else子句')
    print('else子句会在 i<=6为False时执行')

print("i 的值是", i)
print("----------程序退出--------")