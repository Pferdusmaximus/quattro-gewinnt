def check_vertical(board, player):
    rows = len(board) #Anzahl an Reihen
    cols = len(board[0]) #Anzahl an Spalten
    #Zeichen des Spielers ermitteln
    if player == 0:
        chip = "X"
    else:
        chip = "O"

    for col in range(cols):
        count = 0
        for row in range(rows):
            if board[row][col] == chip:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def check_diagonal_down(board, player):
    rows = len(board) #Anzahl an Reihen 
    cols = len(board[0]) #Anzahl an Spalten
    #Zeichen des Spielers ermitteln
    if player == 0:
        chip = "X"
    else:
        chip = "O"

    for row in range(rows- 3):
        for col in range(cols - 3):
            if (board[row][col] == chip and board[row+1][col+1] == chip and board[row+2][col+2] == chip and board[row+3][col+3]) == chip:
                return True
    return False

def check_diagonal_up(board, player):
    rows = len(board) #Anzahl an Reihen
    cols = len(board[0]) #Anzahl an Spalten
    #Zeichen des Spielers ermitteln
    if player == 0:
        chip = "X"
    else:
        chip = "O"

    for row in range(3, rows):
        for col in range(cols - 3):
            if (board[row][col] == chip and board[row-1][col+1] == chip and board[row-2][col+2] == chip and board[row-3][col+3]) == chip:
                return True
    return False