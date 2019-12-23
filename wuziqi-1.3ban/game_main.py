import pygame as py

from checker import *
import piece as pe
import botton as bt


list_QPZB = []  # 棋盘坐标
fps = 100
start_game = False
end_game = False

def init_game():
    py.init()
    py.mixer.init()
    py.mixer.music.load("和平天下.mp3")
    py.mixer.music.play(-1, 0.0)
    pe.qipan(list_QPZB)  # 初始化棋盘
    global ch
    ch = Checker()  # 创建一个对象
    ch.show()  # 显示棋盘


def main():
    init_game()
    running = True
    fcc = py.time.Clock()
    count_num = 0
    global start_game,end_game
    while running:
        fcc.tick(fps)
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                x, y = py.mouse.get_pos()
                if bt.gmstart(x,y):  # 开始游戏
                    start_game = True
                elif bt.gmend(x,y):  # 结束游戏
                    end_game = True
                elif bt.gmagain(x,y):  # 重新开始
                    pe.qipan(list_QPZB)
                    count_num = 0
                    ch.show()  # 显示棋盘
                    start_game = True

                if start_game == True:
                    value = pe.abc(x, y, list_QPZB)
                    if value:  # 鼠标点中位置在棋盘规定范围，进行处理；否则不做处理
                        count_num += 1
                        ch.work(value)
                    if count_num >= 9:  # 当总棋子数大于9时才开始判断输赢
                        if ch.win(pe.judge(list_QPZB)):  # 判断游戏输赢
                            start_game = False

            if event.type == py.QUIT or end_game == True:  # 结束退出游戏
                py.quit()
                running = False
                exit()

if __name__ == '__main__':
    main()
