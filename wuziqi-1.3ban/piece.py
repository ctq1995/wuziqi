
"""
2.棋子：白棋，黑棋
功能：
    1.棋盘点位运算qipan()
    2.棋子落子点位处理abc()
    3.输赢判断judge()
Qi_zi = 1  # 1=白棋，2=黑棋
"""

Qizi = 1  # 1 白棋 2 黑棋

def qipan(list1):  # 初始化棋盘坐标
    list1.clear()  # 清空列表，确保每次初始化，列表长度一致
    for i in range(1,16):
        list_line = []  # 每行交叉点
        for j in range(1,16):
            point_x = j * 40
            point_y = i * 40
            po = (point_x, point_y, 0)
            list_line.append(po)
        list1.append(list_line)  # 总交叉点

def abc(x,y,list1):
    global Qizi
    i = j = 0
    for temp in list1:
        for pos in temp:
            if x >= pos[0] - 10 and x <= pos[0] + 10 and y >= pos[1] - 10 and y <= pos[1] + 10:
                if pos[2] == 0 and Qizi == 1:
                    work = (pos[0], pos[1], 1)
                    list1[j][i] = work   # 改变棋盘点位列表，一个点只能放一个棋子
                    Qizi = 2  # 切换成黑棋
                    return work
                elif pos[2] == 0 and Qizi == 2:
                    work = (pos[0], pos[1], 2)
                    list1[j][i] = work
                    Qizi = 1  # 切换成白棋
                    return work
            i += 1
        j += 1
        i = 0

def judge(list1):   # 输赢判断函数
    count = 0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if j <= len(list1[i])-5:
                # 横向判断
                if list1[i][j][2] == 1 and list1[i][j+1][2] ==1 and list1[i][j+2][2] ==1 and list1[i][j+3][2] ==1 \
                        and list1[i][j+4][2] == 1:
                    return 1
                elif list1[i][j][2] == 2 and list1[i][j+1][2] ==2 and list1[i][j+2][2] == 2 and list1[i][j+3][2] == 2 \
                        and list1[i][j+4][2] == 2:
                    return 2
            if i <= len(list1)-5:
                # 竖向判断
                if list1[i][j][2] ==1 and list1[i+1][j][2] ==1 and list1[i+2][j][2] ==1 and list1[i+3][j][2] == 1 \
                        and list1[i+4][j][2] == 1:
                    return 1
                elif list1[i][j][2] ==2 and list1[i+1][j][2] ==2 and list1[i+2][j][2] ==2 and list1[i+3][j][2] == 2 \
                        and list1[i+4][j][2] == 2:
                    return 2
            if i <= (len(list1)-5) and j <= (len(list1[i])-5):
                # 到右下角判断
                if list1[i][j][2] == 1 and list1[i + 1][j + 1][2] == 1 and list1[i + 2][j + 2][2] == 1 and \
                        list1[i + 3][j + 3][2] == 1 and list1[i + 4][j + 4][2] == 1:
                    return 1
                elif list1[i][j][2] == 2 and list1[i + 1][j + 1][2] == 2 and list1[i + 2][j + 2][2] == 2 and \
                        list1[i + 3][j + 3][2] == 2 and list1[i + 4][j + 4][2] == 2:
                    return 2
            if 4 <= i <= len(list1)-1 and j <= (len(list1[i])-5):
                # 到左下角判断
                if list1[i][j][2] == 1 and list1[i - 1][j + 1][2] == 1 and list1[i - 2][j + 2][2] == 1 and \
                        list1[i - 3][j + 3][2] == 1 and list1[i - 4][j + 4][2] == 1:
                    return 1
                elif list1[i][j][2] == 2 and list1[i - 1][j + 1][2] == 2 and list1[i - 2][j + 2][2] == 2 and \
                        list1[i - 3][j + 3][2] == 2 and list1[i - 4][j + 4][2] == 2:
                    return 2
            if list1[i][j][2] == 1 or list1[i][j][2] == 2:
                count += 1
                if count == 255:
                    return 3
        # print(len(list1))
        # print(len(list1[i]))