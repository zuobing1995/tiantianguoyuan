# 2. 写一个lambda表达式,返两个形参的最大值
#   def mymax(x, y):
#       ...
#   mymax = lambda .....
#   print(mymax(100, 200))  # 200


# def mymax(x, y):
#     return max(x, y)
#     if x > y:
#         return x
#     return y

# mymax = lambda x, y: x if x > y else y
mymax = lambda x, y: max(x, y)

print(mymax(100, 200))  # 200
