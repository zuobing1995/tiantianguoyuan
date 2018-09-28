# 练习:
#   定义一个"人"(Human)类
#     class Human:
#         def set_info(self, name, age, address='不详'):
#             '此方法用来给人对象添加姓名，年龄，家庭住址属性'
#             ... # 此处自己实现
#         def show_info(self):
#             '此处显示此人的信息'
#             ... 
#   调用如下:
#     h1 = Human()
#     h1.set_info('小张', 20, '北京市东城区')
#     h2 = Human()
#     h2.set_info('小李', 18)
#     h1.show_info()
#     h2.show_info()


class Human:
    def set_info(self, name, age, address='不详'):
        '此方法用来给人对象添加姓名，年龄，家庭住址属性'
        self.name = name
        self.age = age
        self.addr = address

    def show_info(self):
        '此处显示此人的信息'
        print(self.name, '今年', self.age,
              '家庭地址:', self.addr)


h1 = Human()
h1.set_info('小张', 20, '北京市东城区')
h2 = Human()
h2.set_info('小李', 18)
h1.show_info()
h2.show_info()
