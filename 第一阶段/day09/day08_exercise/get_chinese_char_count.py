# 1. 写一个函数 get_chinese_char_count,此函数实现的
#   功能是从一个给定的字符串中返回中文字符的个数
#   def get_chinese_char_count(x):
#       ...
#   s = input("请输入中英文混合的字符串:")  # hello中国
#   print('您输入的中文的字符个数是:', get_chinese_char_count(s))  # 2


def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count


s = input("请输入中英文混合的字符串:")  # hello中国
print('您输入的中文的字符个数是:', get_chinese_char_count(s))  # 2

