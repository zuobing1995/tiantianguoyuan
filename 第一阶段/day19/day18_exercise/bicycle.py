# 2. 写一个类Bicycle类,有run方法,调用时显示骑行的里程(km)
#   class Bicycle:
#       def run(self, km):
#           print("自行车骑行了", km, '公里')
# 再写一个类EBicycle,在Bicycle类的基础上添加电池电量volume属性,和两个方法:
#    1.fill_charge(vol) 用来充电 vol 为电量(度)
#    2. run(km) 方法每骑行10km消耗电量1度, 同时显示当前电量,当电量耗尽时,则调用Bicycle的run方法继续骑行
#    class EBicycle(Bicycle):
#         ....
#         def fill_charge(self, vol):
#              '''充电'''

#         def run(self, km):
#             ...
#   b = EBicycle(5) 新买的电动车内有5度电
#   b.run(10)  # 电动骑行了10km还剩4度电
#   b.run(100)  # 电动骑行了40km还剩0度电, 用脚登骑行了60km
#   b.fill_charge(10)  # 充电10度
#   b.run(50)  # 电动骑行了50km还剩5度电


class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, '公里')


class EBicycle(Bicycle):
    def __init__(self, vol):
        self.volume = vol  # 初始电量

    def fill_charge(self, vol):
        '''充电'''
        self.volume += vol

    def run(self, km):
        e_km = min(km, self.volume * 10)  # 算出电能走的最大公里数
        if e_km > 0:
            self.volume -= e_km / 10
            print("电动骑行了%dkm,还剩%.1f度电" % (e_km, self.volume))
        if km > e_km:
            super().run(km - e_km)

b = EBicycle(5)  # 新买的电动车内有5度电
b.run(10)  # 电动骑行了10km还剩4度电
b.run(100)  # 电动骑行了40km还剩0度电, 用脚登骑行了60km
b.fill_charge(10)  # 充电10度
b.run(50)  # 电动骑行了50km还剩5度电
