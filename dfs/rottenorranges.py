ROW = [0,-1,0,1]
COL = [-1,0,1,0]

def issafe(i,j,visited,m):
    return i>=0 and i<=len(m)-1 and j>=0 and j<=len(m[0])-1 and m[i][j]==1 and visited[i][j]==0

def dfs(m,i,j,visited):
    visited[i][j]=1
    m[i][j]=2
    for k in range(4):
        if issafe(i+ROW[k],j+COL[k],visited,m):
            dfs(m,i+ROW[k],j+COL[k],visited)



def rottenorange(m):
    row = len(m)
    col = len(m[0])
    visited =[[0 for i in range(col)] for j in range(row)]
    # print(visited)
    for i in range(row):
        for j in range(col):
            if m[i][j]==2 and visited[i][j]==0:
                dfs(m,i,j,visited)

    print(m)













m= [[2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]]
rottenorange(m)



#################################3 using bfs ##############################################################


from collections import deque

class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
		
        def bfs():
            q = deque()
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 2:
                        q.append((0, x, y))
    
            res = 0
            while q:
                level, x0, y0 = q.popleft()
                res = level

                for dx, dy in d:
                    x, y = x0 + dx, y0 + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((level + 1, x, y))
            return res
			
        res = bfs()
		
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
        return res






















