class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #2d seen array to mark node as seen or unseen
        #dfs traversal on every node 
        #increment island count
        #return island count
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n  for _ in range(m)]
        directions = [[0,1] , [0,-1] , [1,0] , [-1,0]]
        islands=0

        def dfs(r , c):
            seen[r][c]= True
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<= nr< m and 0 <= nc < n and not seen[nr][nc] and grid[nr][nc] == "1":
                    dfs(nr , nc)
                 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not seen[row][col]:
                    islands+=1
                    dfs(row,col)
        return islands
                    


