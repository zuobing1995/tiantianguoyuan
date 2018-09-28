# try_embed.py


# 此示例示意try语句嵌套,在内层的try语句如果已经把状态转为正常状态
# 则外层的try语句将收不到错误通知

try:
    try:
        n = int(input("请输入整数:"))
    except ValueError:
        print("在内层try语句内出现值错误,已转为正常状态")
    else:
        print("内层try语句没有出现异常")
except:
    print('外层的try语句接收到的异常通知.已处理并转为正常状态')
else:
    print("外层try语句没有出现异常")



