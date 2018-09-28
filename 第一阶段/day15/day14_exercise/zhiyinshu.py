# 2. 分解质因数: 输入一个正整数，分解质因数:
#   如输入:
#     90
#   则打印:
#     '90=2*3*3*5'
#     (质因数是指小数最小能被原数整除的素数(不包含1))


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


L = []  # 此列表用存储素数（质因数)
n = int(input("请输入一个正整数: "))
number = n # 保存原有的数

# 判断如果n不为1则找质因数
while n != 1:
    for i in range(2, n + 1):
        # 依次让n除以i,如果整数则i为质因数
        if n % i == 0 and is_prime(i):
            L.append(i)
            n = int(n / i)
            break  # 查找当前一个质固数结束

print(L)
print(number, "=", '*'.join([str(x) for x in L]),
      sep='')
















