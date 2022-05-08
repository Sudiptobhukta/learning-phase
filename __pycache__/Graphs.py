import queue
class graphs:
    # this is the graph building 
    def __init__(self,nVerticies):
        self.nVert = nVerticies
        self.board = [[0 for i in range(self.nVert)]for j in range(self.nVert)]

    def addVal(self,row,col):
        self.board[row][col]=1
        self.board[row][col]=1

    def removeVal(self,row,col):
        if self.containEdge(row,col) is False:
            self.board[row][col]=0
            self.board[col][row]=0

    def containEdge(self,row,col):
        return True if (self.board[row][col]>0) else False
    

    # now this is the DFS
    def dfsHelper(self,val,visted):
        print(val)
        visted[val]=True
        for i in range(self.nVert):
            if self.board[val][i]>0 and visted[i] is False:
                self.dfsHelper(i,visted)

    def dfs(self):
        visted =[False for i in range(self.nVert)]
        self.dfsHelper(0,visted)


    
    #now this is the BFS
    def bfs(self):
        q = queue.Queue()
        visited = [False for i in range(self.nVert)]
        q.put(0)
        visited[0]=True
        while q.empty() is False:
            value = q.get()
            print(value)
            for i in range(self.nVert):
                if self.board[value][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
    
    def __str__(self) -> str:
        return str(self.board)


g= graphs(5)
g.addVal(0,1)
g.addVal(1,3)
g.addVal(2,4)
g.addVal(0,2)
g.bfs()