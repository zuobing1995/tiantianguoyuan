# break_while_embed.py

i = 1
while i <= 10:
    j = 1
    while j <= 20:
        print(j, end=' ')
        if j == 15:
            break
        j += 1
    print()
    i += 1

print("程序结束")
