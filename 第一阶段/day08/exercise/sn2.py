# 2. 编写函数fun2,计算下列多项式的和
#   Sn = 1/(1*2) + 1/(2*3) + 1/(3*4) +
#             ... + 1/(n*(n+1)) 的和

#   print(fun2(3))  # 0.75
#   print(fun2(1000))  


def fun2(n):
    s = 0
    for x in range(1, n + 1):
        s += 1 / (x * (x + 1))
    return s

print(fun2(3))  # 0.75
print(fun2(1000))  
