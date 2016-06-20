res = []
#http://www.cnblogs.com/bigbigtree/p/3889591.html
def nQueens(n):
    if n == 0:
        return []
    board = [0] * n
    #board[i] means there is a queen at (i, board[i])
    generate(board, n, 0)
    return res

def generate(board, n, index):
    for i in range(n):
        if isValid(board, index, i):
            board[index] = i
            if index == n - 1:
                addRes(board)
                board[index] = 0
                return
            generate(board, n, index + 1)
            board[index] = 0

def addRes(board):
    solution = []
    for i in range(len(board)):
        row = ["."] * len(board)
        row[board[i]] = 'Q'
        solution.append("".join(row))
    res.append(solution)

def isValid(board, row, col):
    for i in range(row):
        tcol = board[i]
        if tcol == col: #Same column
            return False
        if tcol - col == i - row: #same row
            return False
        if tcol - col == row - i: #same diagnol
            return False
    return True

print nQueens(4)



