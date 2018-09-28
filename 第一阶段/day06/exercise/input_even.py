# 练习:
#   输入一个开始的整数用begin绑定
#   输入一个结束的整数用end绑定
#   将从begin开始,到end结束(不包含end)的所有偶数存于列表中
#   并打印此列表
#   (可以使用列表推导式完成,也可以用循环语句来完成)
  
begin = int(input("请输入开始的整数: "))
end = int(input("请输入结束的整数: "))
L = [x for x in range(begin, end) if x % 2 == 0]
print(L)

L2 = []
for x in range(begin, end):
    if x % 2 == 0:
        L2.append(x)

print("L2=", L2)
