# test_except.py

try:
    n = int(input("请输入整数:"))
except int:  # 错误，int类型不能当成错误类型用于try-except语句中
    pass



