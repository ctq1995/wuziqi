"""
控制各种按钮功能
"""

def gmstart(x,y):  # 开始按钮
    if 645 < x < 790 and 350 < y < 410:
        # print('请开始游戏')
        return 1

def gmagain(x,y):  # 重新开始游戏
    if 645 < x < 790 and 450 < y < 510:
        # print('重新开始游戏')
        return 1

def gmend(x,y):  # 结束按钮
    if 645 < x < 790 and 550 < y < 610:
        return 1