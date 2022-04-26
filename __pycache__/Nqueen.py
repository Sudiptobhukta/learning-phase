def printPath(n):
    board = [[0 for i in range(n)] for j in range(n)]
    printHelper(0,n,board)

def printHelper(row,n,board):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        return

    for col in range(n):
        if isSafe(row,col,board,n) is True:
            board[row][col]=1
            printHelper(row+1,n,board)
            board[row][col]=0
    return

def isSafe(row,col,board,n):

    # vertical check
    i=row-1
    while i>=0:
        if board[i][col]==1:
            return False
        i-=1
    
    # left Diagonal check
    i= row-1
    j= col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    # right diagonal check
    i=row-1
    j=col+1

    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    return True

n=int(input("Enter the size of the matrix: "))
printPath(n)



