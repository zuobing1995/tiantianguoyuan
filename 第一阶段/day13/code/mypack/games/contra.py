# mypack/games/contra.py


def play():
    print("正在玩 魂斗罗....")


def gameover():
    '''此函数会在游戏结束时调用
    　　　然后此时函数调用菜单 mypack.menu 里的show_menu
    '''
    print("game over!")
    # 绝对导入:
    # 1) import mypack.menu 
    # 　　　mypack.menu.show_menu()
    # 2) from mypack.menu import show_menu
    #    show_menu()
    # 3) from mypack.menu import *
    #    show_menu()
    # 相对导入
    # 1) from ..menu import show_menu
    from ..menu import *
    show_menu()


print("魂斗罗 模块被加载")

