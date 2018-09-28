# 2. 写一个实现迭代器协议的类,让此类可以生成从b 开始的n个素数
#   class Prime:
#       def __init__(self, b, n):
#           ...
#       def __iter__(self):
#          ....

#   L = [x for x in Prime(10, 4)]
#   print(L)  # L = [11, 13, 17, 19]


class Prime:
    def __init__(self, b, n):
        self.begin = b
        self.count = n

    def __iter__(self):
        return PrimeIterator(self.begin, self.count)


class PrimeIterator:
    def __init__(self, b, n):
        self.begin = b  # 开始时起始数字
        self.count = n  # 需要创建的数据的个数
        self.cur_count = 0  # 表示已经生成了的素数的个数

    def __isprime(self, x):
        '''用来判断x是否是素数'''
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def __next__(self):
        # 判断已提供数据的数据个数,和要提供的数据个数来决定是否终止
        if self.cur_count >= self.count:
            raise StopIteration
        while True:
            if self.__isprime(self.begin):
                # 得到下一个素数
                r = self.begin
                # 然后把self.begin 加1
                self.begin += 1
                # 已生成个数要加1
                self.cur_count += 1
                # 返回当前的素数
                return r
            self.begin += 1  # 准备判断下一个数是否为素数


# L = []
# it = iter(Prime(10, 4))
# while True:
#     try:
#         x = next(it)
#         L.append(x)
#     except StopIteration:
#         break
# print(L)

L = [x for x in Prime(10, 4)]
print(L)  # L = [11, 13, 17, 19]
