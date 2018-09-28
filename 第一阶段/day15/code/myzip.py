# myzip.py

def myzip(iter1, iter2):
    it1 = iter(iter1)  # 拿到两个对象的迭代器
    it2 = iter(iter2)
    while True:
        try:
            t = (next(it1), next(it2))  # StopIteration
            yield t
        except StopIteration:
            break


numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']

for t in myzip(numbers, names):
    print(t)


