# class_variable.py


# 此示例示意类变量的定义和用法
class Human:
    total_count = 0  # 类变量，用来记录Human对象的个数
    pass


print(Human.total_count)  # 0 访问类变量
h1 = Human()  # 创建一个对象

print(h1.total_count)  # 0 借助于此类的实例访问类变量(类属性)

h1.total_count = 10000  # 这一步为实例添加实例属性
print(h1.total_count)  # 10000
print(Human.total_count)  # 0

#类变量可以通过此类的对象的__class__属性间接访问
h1.__class__.total_count += 1  # 等同于Human.total_count += 1
print(Human.total_count)  # 1

# Human.total_count += 1  # 改变类变量
# print(Human.total_count)  # 1





# print(dir())