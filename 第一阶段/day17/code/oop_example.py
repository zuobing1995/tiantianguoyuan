# oop_example.py

# 此示例示意用面向对象编程实现对象与对象之间的关系的描述

# 面向对象的综合示例:
#   有两个人:
#    　属性:
#       1. 姓名: 张三, 年龄 35 岁
#       2. 姓名: 李四, 年龄 8 岁
#     行为:
#       1. 教别人学东西　teach
#       2. 工作赚钱 work
#       3. 借钱 borrow 
#   事情:
#     张三　教　李四 学 python
#     李四　教　张三　学 王者荣耀
#     张三　上班赚了 1000　元钱
#     李四　向 张三　借了 200 元钱
#     35　岁的　张三　有钱 800元，它学会的技能: 王者荣耀
#     8 岁的 李四 有钱 200元， 它学会的技能: python


# 有两个人:

#   行为:
#     1. 教别人学东西　teach
#     2. 工作赚钱 work
#     3. 借钱 borrow


class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱数为0
        self.skill = []  # 技能列表

    def teach(self, other, skill):
        print(self.name, '教', other.name, '学', skill)
        other.skill.append(skill)  # 让other增加技能

    def work(self, m):
        print(self.name, '上班赚了', m, '元钱')
        self.money += m

    def borrow(self, other, m):
        if other.money > m:
            print(self.name, '向', other.name, '借', m, '元钱')
            other.money -= m
            self.money += m
        else:
            print(other.name, '没有借钱给', self.name)

    def show_info(self):
        print(self.age, '岁的', self.name,
              '有钱', self.money, '元，它学会的技能:',
              '、'.join(self.skill))


zhang3 = Human('张三', 35)
li4 = Human('李四', 8)
# 张三　教　李四 学 python
zhang3.teach(li4, 'Python')
# 李四　教　张三　学 王者荣耀
li4.teach(zhang3, '王者荣耀')
# # 张三　上班赚了 1000　元钱
zhang3.work(1000)
# 李四　向 张三　借了 200 元钱
li4.borrow(zhang3, 200)
# 35　岁的　张三　有钱 800元，它学会的技能: 王者荣耀
zhang3.show_info()
# 8 岁的 李四 有钱 200元， 它学会的技能: python
li4.show_info()
