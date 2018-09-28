# gen_vs_list_comprehension.py

L = [2, 3, 5, 7]
L2 = [x ** 2 + 1 for x in L]
it = iter(L2)
print(next(it))  # 5
L[1] = 30
print(next(it))  # 10

# 以下是生成器表达式
L = [2, 3, 5, 7]
gen = (x ** 2 + 1 for x in L)
it = iter(gen)
print(next(it))  # 5
L[1] = 30
print(next(it))  # 901
