# instance_method.py


# 此示例示意实例方法的定义和调用
class Dog:
    '''创建一个Dog类,此类用于描述一种
    小动物的行为和属性'''
    def eat(self, food):
        '''此方法用来描述小狗吃东西的行为'''
        print("id为:", id(self), '的小狗正在吃', food)
    def sleep(self, hour):
        print("小狗睡了", hour, '小时')
    def play(self, obj):
        print("小狗正玩", obj)


dog1 = Dog()  # 创建一个小狗对象
dog1.eat('骨头')
dog1.sleep(1)
dog1.play('球')


dog2 = Dog()  # 创建另外一只狗对象
dog2.eat('狗粮')
dog2.sleep(3)
dog2.play('飞盘')



