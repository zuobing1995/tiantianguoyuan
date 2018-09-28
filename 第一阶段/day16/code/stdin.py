# stdin.py

# 此示例示意标准输入文件 sys.stdin 的用法

import sys

s = sys.stdin.readline()
print(s)

sys.stdin.close()  # 关闭标准输入文件则input函数就不能用了

s2 = input("请输入:")
print(s2)