# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        elapsed = 0
        queue = deque([(i,j)\
        for i in range(rows)\
        for j in range(cols)\
        if grid[i][j] == 2])

        while queue:
            l = len(queue)
            for _ in range(l):
                y,x = queue.popleft()

                for i in range(max(0, y-1), min(y+2, rows)):
                    if grid[i][x] == 1:
                        grid[i][x] = 2
                        queue.append((i,x))
                    
                for j in range(max(0, x-1), min(x+2, cols)):
                    if grid[y][j] == 1:
                        grid[y][j] = 2
                        queue.append((y,j))

            elapsed += 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return elapsed-1 if elapsed else 0