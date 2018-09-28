L = []


print("id(L)=", id(L))
def input_number():
    L2 = []
    while True:
        n = int(input("请输入正整数: "))  # 1 2 3 4
        if n < 0:
            break
        L2.append(n)
    # L = L2  # 创建局部变量,未改变全局变量L的绑定关系
    # L.extend(L2)  # 根据变量找到列表,改变的是列表而不是变量
    # L += L2  # 出错  L = L + L2
    return L2

input_number()
print(L)  # 打印什么?
print('id(L)=', id(L))