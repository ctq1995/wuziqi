
"""
1.棋盘类：背景，方格，按钮
功能：
    1.初始化棋盘参数
    2.绘制棋盘网格
    3.显示棋子位置
    4.输赢显示
"""
import pygame as py


background = py.image.load('234.jpg')  # 背景
black = py.image.load('storn_black.png')  # 黑棋
white = py.image.load('storn_white.png')  # 白棋
win_black = py.image.load('1.png')  # 黑棋胜利
win_white = py.image.load('2.png')  # 白棋胜利
win_draw = py.image.load('3.png')  # 平局

class Checker:
    def __init__(self):
        self.line_color = (0,0,0)   # 网格颜色
        self.screen =py.display.set_mode((850, 640))
        self.font = py.font.Font('simkai.ttf', 35)
        self.value = 1

    def framing(self):   # 制作棋盘
        self.screen.blit(background,(0,0))
        # 棋盘网格
        for i in range(1, 16):
            py.draw.line(self.screen, self.line_color, (40 * i, 40), (40 * i, 600))
            py.draw.line(self.screen, self.line_color, (40, 40 * i), (600, 40 * i))
        # 四条边线
        py.draw.line(self.screen, self.line_color, (40, 40), (600, 40), 3)
        py.draw.line(self.screen, self.line_color, (40, 40), (40, 600), 3)
        py.draw.line(self.screen, self.line_color, (600, 40), (600, 600), 3)
        py.draw.line(self.screen, self.line_color, (40, 600), (600, 600), 3)
        # 棋盘五个点
        py.draw.circle(self.screen, self.line_color, (160, 160), 5)
        py.draw.circle(self.screen, self.line_color, (480, 160), 5)
        py.draw.circle(self.screen, self.line_color, (320, 320), 5)  # 棋盘中心点
        py.draw.circle(self.screen, self.line_color, (160, 480), 5)
        py.draw.circle(self.screen, self.line_color, (480, 480), 5)
        # 棋盘标识
        # 创建三个按钮框
        # py.draw.rect(self.screen, self.line_color, [640, 350, 150, 60], 2)
        # py.draw.rect(self.screen, self.line_color, [640, 450, 150, 60], 2)
        # py.draw.rect(self.screen, self.line_color, [640, 550, 150, 60], 2)
        # 加文本文字
        text1 = self.font.render('开始游戏', True, self.line_color)
        text2 = self.font.render('重新开始', True, self.line_color)
        text3 = self.font.render('结束游戏', True, self.line_color)
        self.screen.blit(text1, (645, 360))
        self.screen.blit(text2, (645, 460))
        self.screen.blit(text3, (645, 560))

    def show(self):
        self.framing()
        py.display.set_caption('五子棋' + '--双人对战版')  # 设置窗口标题
        py.display.flip()  # 刷新当前窗口

    def work(self,value):
        if value[2] == 1:
            self.screen.blit(white,(value[0]-18,value[1]-18))
        else:
            self.screen.blit(black,(value[0]-18,value[1]-18))
        py.display.flip()


    def win(self,value):
        if value == 1:
            self.screen.blit(win_white, (50, 50))
            py.display.flip()
            return True
        elif value == 2:
            self.screen.blit(win_black,(50,50))
            py.display.flip()
            return True
        elif value == 3:
            self.screen.blit(win_draw,(50,50))
            py.display.flip()
            return True

