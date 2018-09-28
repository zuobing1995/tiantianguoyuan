# 练习:
#   经理有: 曹操，刘备，孙权
#   技术员有: 曹操，孙权，张飞，关羽
#   用集合求:
#     1. 即是经理也是技术员的有谁?
#     2. 是经理，但不是技术人员的都有谁?
#     3. 是技术人员，但不是经理的都有谁?
#     4.　张飞是经理吗？
# 　　　　5. 身兼一职的人都有谁?
#     6. 经理和技术员共有几个人?


managers = {'曹操', '刘备', '孙权'}
techs = {'曹操', '孙权', '张飞', '关羽'}

print("即是经理也是技术员的有:", managers & techs)
print("是经理，但不是技术人员的都有:", managers - techs)
print("是技术人员，但不是经理的都有:", techs - managers)
if '张飞' in managers:
    print("张飞是经理")
else:
    print("张飞不是经理")

print("身兼一职的人都有", managers ^ techs)
print("经理和技术员共有%d个人" % len(managers | techs))


