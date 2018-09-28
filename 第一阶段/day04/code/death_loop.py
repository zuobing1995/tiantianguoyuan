# death_loop.py


# 此示例来示意死循环的用法

# 循环输入字符串,当输入'quit()' 结束输入
# 将每次输入的内容打印在屏幕上

while True:
    s = input("请输入:>>> ")
    if s == 'quit()':
        break
    print("您刚才输入的是:", s)
else:
    print("我是while语句的 else子句,我永远不会被执行")
print("程序结束")








