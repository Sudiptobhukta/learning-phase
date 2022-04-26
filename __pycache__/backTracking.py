def printPath(maze):
    n=len(maze)
    sol=[[0 for i in range(n)] for j in range(n)]
    printPathHelper(0,0,maze,n,sol)

def printPathHelper(x,y,maze,n,sol):
    if x==n-1 and y==n-1:
        sol[x][y]==1
        print(sol)
        return
    
    if x<0 or y<0  or x>=n or y >=n or sol[x][y] == 1 or maze[x][y]==0:
        return

    sol[x][y]=1
    printPathHelper(x+1,y,maze,n,sol)
    printPathHelper(x,y+1,maze,n,sol)
    printPathHelper(x-1,y,maze,n,sol)
    printPathHelper(x,y-1,maze,n,sol)
    sol[x][y]=0
    return


n=int(input())
maze=[]
for i in range(n):
    row=[int(ele) for ele in input().split()]
    maze.append(row)

printPath(maze) 