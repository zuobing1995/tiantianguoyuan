# poly.py


class Shape:
    def draw(self):
        print("Shape的draw()被调用")


class Point(Shape):
    def draw(self):
        print('正在画一个点!')


class Circle(Point):
    def draw(self):
        print('正在画一个圆!!!')


def my_draw(s):
    s.draw()  # <<<--- 此处显示出多态中的"动态"


s1 = Circle()  # 创建一个圆对象
s2 = Point()  # 创建一个点对象
my_draw(s1)
my_draw(s2)
