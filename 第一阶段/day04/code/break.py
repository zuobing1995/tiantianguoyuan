# break.py

i = 1
while i <= 6:
    print('循环开始时:', i)
    if i == 3:
        break

    print('循环结束时:', i)
    i += 1

print("i 的值是", i)
print("----------程序退出--------")