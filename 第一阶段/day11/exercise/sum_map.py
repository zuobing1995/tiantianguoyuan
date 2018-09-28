# 练习　：
# 　　1. 求: 1**2 + 2**2 + 3**2 + .... + 9**2的和　
# 　　2. 求: 1**3 + 2**3 + 3**3 + .... + 9**3的和　



# 1. 求: 1**2 + 2**2 + 3**2 + .... + 9**2的和
# 方法1
def power2(x):
    # print("power2被调用!, x=", x)
    return x ** 2

s = 0  # 用来保存和
for x in map(power2, range(1, 10)):
    s += x
print(s)

# 方法2
s = 0
for x in map(lambda x: x ** 2, range(1, 10)):
    s += x
print(s)

# 方法３
print(sum(map(lambda x: x**2, range(1, 10))))

# 2. 求: 1**3 + 2**3 + 3**3 + .... + 9**3的和
print(sum(map(lambda x: x**3, range(1, 10))))

