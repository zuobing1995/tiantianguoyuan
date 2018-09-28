# 1. 将 1 ~ 20的偶数用filter生成可迭代对象后，将可迭代
# 　　　对象生成的数据存于列表中
# 　　最终结果:
#     L = [2, 4, 6, 8, ... 18, 20]


def iseven(x):  # 判断x是否是偶数，是偶数返回True,...
    if x % 2 == 0:
        return True
    return False


# L = list(filter(iseven, range(1, 21)))
L = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(L)



