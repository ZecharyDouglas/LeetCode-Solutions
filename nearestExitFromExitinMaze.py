from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #bfs implemented used an deque
        start_row, start_col = entrance
        seen ={(start_row,start_col)}
        steps=0
        #directions array of tuples for each possible direction in x/y planes
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        #queue's elements are index of a node with the steps for that level
        queue = deque([(start_row, start_col , steps)])
        
        while queue:
            row , col , steps = queue.popleft()
            #if the current node is an exit then return the steps
            #exits are not the entrance , and on one of the 4 margins of the grid
            if ([row , col] != entrance) and (row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1 ):
                return steps
            #create and test the neighbors 
            for dr , dc in directions:
                nr = row + dr
                nc = col + dc
                #check if the neighbors are in bounds , empty cells , and not seen if they are then add them to seen and the queue
                if 0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc] =="." and (nr , nc) not in seen:
                    queue.append((nr , nc , steps+1))
                    seen.add((nr,nc))
        return -1
            
            