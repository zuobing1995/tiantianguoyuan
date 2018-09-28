# eval.py

x = 100
y = 200
s = "x + y"

a = eval(s)  # 解释执行s字符串,把表达式的值返回回来
print(a)  # 300

b = eval(s, None, {'x': 1, 'y': 2})
print(b)

c = eval(s, {'x': 10, 'y': 20}, {'x': 1})
print(c)  # 21

