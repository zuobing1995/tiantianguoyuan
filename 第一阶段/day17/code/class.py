# class.py


class Dog:
    '''创建一个Dog类,此类用于描述一种
    小动物的行为和属性'''
    pass


dog1 = Dog()  # 创建Dog类的一个实例
print(id(dog1))

dog2 = Dog()  # 创建Dog类的第二个实例
print(id(dog2))

print('--------------------')
# 对比
lst1 = list()  # 创建一个空列表
print(id(lst1))

lst2 = list()  # 创建另一个空列表
print(id(lst2))


