# multiple_inherit.py


# 此示例示意多继承的定义语法的基本用法
class Car:
    '''汽车类'''
    def run(self, speed):
        print("汽车以", speed, '公里/小时的速度行驶')


class Plane:
    '''飞机类'''
    def fly(self, height):
        print("飞机以海拔", height, '米的高度飞行')


class PlaneCar(Car, Plane):
    '''PlaneCar类同时继承自汽车类和飞机类'''


p = PlaneCar()  # 创建一个飞行汽车对象
p.fly(10000)
p.run(300)










 