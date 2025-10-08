from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #the idea is to find connected components that have no nodes on the edges
        #seen array/list 
        #traverse through grid and run bfs function on a 0 node 
        rows = len(grid)
        cols = len(grid[0])
        seen = [[0 for _ in range(cols)] for _ in range(rows) ]
        dirs = [(-1,0) , (1,0) ,(0,-1) , (0,1)]
        ans=0
        def bfs(node):
            queue = deque([node])
            [sy, sx] = node
            seen[sy][sx] = 1
            closed = 1  # 1 means closed; flip to 0 if we touch a border

            while len(queue) > 0:
                [node_y, node_x] = queue.popleft()

                # if on border, it's not closed
                if node_y == 0 or node_y == rows - 1 or node_x == 0 or node_x == cols - 1:
                    closed = 0

                for r, c in dirs:
                    ny, nx = node_y + r, node_x + c
                    if 0 <= ny < rows and 0 <= nx < cols:
                        if seen[ny][nx] == 0 and grid[ny][nx] == 0:
                            seen[ny][nx] = 1
                            queue.append([ny, nx])
            return closed
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and seen[r][c] == 0:
                    ans += bfs([r, c])

        return ans
                

