board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

def isValidSudoku(board):
    check = 9*[False]
    valid = True

    #checando linhas
    for k in range(9):
        for j in range(9):
            if ord(board[k][j]) >= 49 and ord(board[k][j]) <= 57:
                if check[int(board[k][j]) - 1] == False:
                    check[int(board[k][j]) - 1] = True
                elif check[int(board[k][j]) - 1] == True:
                    return False
        check = 9*[False]

    check = 9*[False]

    #checando colunas
    for k in range(9):
        for j in range(9):
            if ord(board[j][k]) >= 49 and ord(board[j][k]) <= 57:
                if check[int(board[j][k]) - 1] == False:
                    check[int(board[j][k]) - 1] = True
                elif check[int(board[j][k]) - 1] == True:
                    return False
        check = 9*[False]
    
    check = 9*[False]

    #checando blocos
    for l in range(9):
        offsets = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        offset1 = offsets[l][0]
        offset2 = offsets[l][1]
        for k in range(3):
            for j in range(3):
                item = board[k+offset1][j+offset2]
                if ord(item) >= 49 and ord(item) <= 57:
                    if check[int(item) - 1] == False:
                        check[int(item) - 1]  = True
                    elif check[int(item) - 1]  == True:
                        return False
        check = 9*[False]

    return valid

print(isValidSudoku(board))