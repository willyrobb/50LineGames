import os
def clear():
    os.system('cls')
board = [[0,0,0],[0,0,0],[0,0,0]]
def printBoard():
    for rows in board:
        print(rows)
def didWin():
    if [board[0][0],board[1][1],board[2][2]] == [board[1][1],board[1][1],board[1][1]] and board[1][1] != 0:
        return True
    for items in board:
        if items == [items[1],items[1],items[1]] and items[1] != 0:
            return True
    for i in range(3):
        rowList = []
        for j in range(3):
            rowList.append(board[j][i])
        if rowList == [rowList[1],rowList[1],rowList[1]] and rowList[1] != 0:
            return True
    return False
turn = 2
while didWin() == False:
    clear(), printBoard()
    if turn == 2: turn =1
    else: turn = 2
    posX = input(f'Player {turn} please choose a y position: ')
    while posX.isdigit() and (int(posX) > 3 or int(posX) < 1):
        posX = input(f'Player {turn} please choose a y position: ')
    posy = input(f'Player {turn} please choose a x position: ')
    while posy.isdigit() and (int(posy) > 3 or int(posy) < 1):
        posy = input(f'Player {turn} please choose a x position: ')
    if board[int(posX) - 1][int(posy) - 1] != 1 and board[int(posX) - 1][int(posy) - 1] != 2:
        board[int(posX) - 1][int(posy) - 1] = turn
    else:
        if turn == 2: turn =1
        else: turn = 2
print(f'Player {turn} wins!')