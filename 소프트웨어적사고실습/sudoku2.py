board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(board, row, col, num):
    for i in range(9):
        if (num == board[row][i]) and i != col:
            return False
    for i in range(9):
        if (num == board[i][col]) and i != row:
            return False
            
    a = []; b = []
    
    if row % 3 == 0: a = [row, row + 1, row + 2]
    elif row % 3 == 1: a = [row - 1, row, row + 1]
    else: a = [row - 2, row - 1, row]
    
    if col % 3 == 0: b = [col, col + 1, col + 2]
    elif col % 3 == 1: b = [col - 1, col, col + 1]
    else: b = [col - 2, col - 1, col]
    
    for i in a:
        for j in b:
            if board[i][j] == num and ((i != row) or (j != col)):
                return False
    return True

def solve_soduku2(board):
    try:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for t in range(1, 10):
                        if is_valid(board, i, j, t):
                            board[i][j] = t
                            solve_soduku2(board)
                            board[i][j] = 0
                    return
        
        print_board(board)
        raise Exception

    except Exception:
        pass

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

solve_soduku2(board)