# 练习:
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据为字符串的反序
#             'moT' 'yrreJ'  'ekipS'  'ekyT'

#   结果:  ['Spike', 'Tyke', 'Tom', 'Jerry']


names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 排序的依据为字符串的反序
#           'moT' 'yrreJ'  'ekipS'  'ekyT'
def k(s):
    return s[::-1]


L = sorted(names, key=k)
print(L)  # ['Spike', 'Tyke', 'Tom', 'Jerry']










