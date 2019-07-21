# GET INPUT

def initBoard(board):
    for i in range(4):
        row = list(map(lambda x: int(x), input().split(" ")))
        board.append(row)
        
# TRANPOSE 4 x 4 BOARD (for moving UP/DOWN)

def transpose(board):
    newBoard  = [[], [], [], []]
    for i in range(4):
        for row in board:
            newBoard[i].append(row[i])
    return newBoard

# LEFT

def moveCellLeft(row, i, addedCells):
    if not i == 0:
        if (row[i-1] == 0):
            row[i-1] = row[i]
            row[i] = 0
            moveCellLeft(row, i-1, addedCells)
        elif(row[i-1] == row[i] and not i-1 in addedCells):
            row[i-1] += row[i]
            row[i] = 0
            addedCells.append(i-1)

def moveRowLeft(row):
    addedCells = []
    for i in range(1, len(row)):
        moveCellLeft(row, i, addedCells)

def moveLeft(board):
    for row in board:
        moveRowLeft(row)

# RIGHT

def moveCellRight(row, i, addedCells):
    if not i == len(row)-1:
        if (row[i+1] == 0):
            row[i+1] = row[i]
            row[i] = 0
            moveCellRight(row, i+1, addedCells)
        elif(row[i+1] == row[i] and not i+1 in addedCells):
            row[i+1] += row[i]
            row[i] = 0
            addedCells.append(i+1)

def moveRowRight(row):
    addedCells = []
    for i in range(len(row)-2, -1, -1):
        moveCellRight(row, i, addedCells)

def moveRight(board):
    for row in board:
        moveRowRight(row)

# DISPLAY BOARD

def printBoard(board):
    for row in board:
        for number in row:
            print(number, end=" ")
        print()

# MAIN

def main():
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    
    board = []
    initBoard(board)
    move = int(input())
    
    if move == LEFT:
        moveLeft(board)
    elif move == RIGHT:
        moveRight(board)
    else:
        board = transpose(board)
        if move == UP:
            moveLeft(board)
        elif move == DOWN:
            moveRight(board)    
        board = transpose(board)
        
    printBoard(board)

if __name__ == "__main__":
    main()