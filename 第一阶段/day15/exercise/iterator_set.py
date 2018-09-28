# 练习:
#   有一个集合:
#      s = {'唐僧', '悟空', '八戒','沙僧'}

#   用for语句来遍历所有元素如下:
#     for x in s:
#         print(x)
#     else:
#         print('遍历结束')
#   将上面的for语句改写为while语句和迭代器实现


s = {'唐僧', '悟空', '八戒', '沙僧'}
# for x in s:
#     print(x)
# else:
#     print('遍历结束')

# 方法1
# myit = iter(s)
# while True:
#     try:
#         x = next(myit)
#         print(x)
#     except StopIteration:
#         print("遍历结束")
#         break

# 方法2
myit = iter(s)
try:
    while True:
        x = next(myit)
        print(x)
except StopIteration:
    print("遍历结束")






