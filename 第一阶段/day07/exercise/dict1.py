# 字典推导式练习:
#   1. 已知有如下字符串列表
#     L = ['tarena', 'xiaozhang', 'abc']
#   生成如下字典:
#     d = {'tarena': 6, 'xiaozhang': 9, 'abc': 3}
#     注: 字典的值为键的长度

L = ['tarena', 'xiaozhang', 'abc']
# d = {'tarena': 6, 'xiaozhang': 9, 'abc': 3}
# 方法1
# d = {}  # 创建一个空字典
# for s in L:
#     d[s] = len(s)

# 方法2
d = {s: len(s) for s in L}

print(d)
