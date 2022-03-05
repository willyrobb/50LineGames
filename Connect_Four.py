import os
def clear():
    os.system('cls')
board = []
for x in range(7):
    board.append([])
    for y in range(6):
        board[x].append(0)
def printBoard():
    for y in range(6):
        line = '|'
        for x in range(7):
            line += str(board[x][y]) + '|'
        print(line)
def dropPeice(row,player):
    rowGrid, space, peiceDropped = board[row], 0, False
    while space < 6 and peiceDropped == False:
        if rowGrid[space] == 1 or rowGrid[space] == 2:
            board[row][space - 1], peiceDropped = player, True
        space += 1
    if peiceDropped == False:
        board[row][5] = player
def checkForWin():
    for rows in board:
        for i in range(3):
            if rows[i:i+4] == [rows[i],rows[i],rows[i],rows[i]] and rows[i] != 0: return False
    for i in range(6):
        for y in range(4):
            list = []
            for add in range(4):
                list.append(board[y + add][i])
            if list == [list[0],list[0],list[0],list[0]] and list[0] != 0: return False
    for x in range(4):
        for y in range(3):
            list, revList = [], []
            for i in range(4):
                list.append(board[x + i][y + i]), revList.append(board[6 - x - i][y + i])
            if (list == [list[0],list[0],list[0],list[0]] and list[0] != 0) or (revList == [revList[0],revList[0],revList[0],revList[0]] and revList[0] != 0):
                return False
    return True
turn = 2
while checkForWin():
    clear(), printBoard()
    if turn == 1: turn = 2
    else: turn = 1
    row = input(f"Player {turn}, select a column to drop in: ")
    while row.isdigit() == False or int(row) < 1 or int(row) > 7:
        row = input(f"Player {turn}, select a column to drop in: ")
    dropPeice(int(row) - 1,turn)
print(f'Player {turn} wins')