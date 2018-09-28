# 2. 已知有如下两个列表:
#   nos = [1001, 1002, 1005, 1008]
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   用上述两个列表生成如下字典:
#   {1001: 'Tom', 1002: 'Jerry', 1005: 'Spike', 1008: 'Tyke'}


nos = [1001, 1002, 1005, 1008]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# d = {k: v for k in nos for v in names}  #错误方法
# 方法1
# d = {}
# for index in range(len(nos)):  # 让range生成索引
#     print(index)  # 0, 1, 2, 3
#     d[nos[index]] = names[index]

# 方法2,用推导式实现
d = {nos[index]: names[index]
     for index in range(len(nos))}

print(d)

# {1001: 'Tom', 1002: 'Jerry', 1005: 'Spike', 1008: 'Tyke'}





