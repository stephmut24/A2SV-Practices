# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r,c, s = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    s += 4
                    if i and grid[i-1][j]:
                        s -= 2
                    if j and grid[i][j-1]:
                        s -= 2
        return s
        