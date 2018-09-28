# test_mypack.py


# 此主模块用来测试和调用mypack包里的模块中的函数　
# import mypack.menu
# mypack.menu.show_menu()  # 第一种调用方式

# from mypack.menu import show_menu
# show_menu()

# import mypack.games.contra
# mypack.games.contra.play()

import mypack.games.contra as c
c.play()

from mypack.games.contra import play
play()

from mypack.games.contra import *
