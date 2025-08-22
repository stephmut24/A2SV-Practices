# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        visited = [[False] * n for _ in range(n)]

        # Step 1: DFS to find and mark the first island
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            grid[x][y] = 2  # Mark the island
            q.append((x, y))  # Add to queue for BFS later
            for dx, dy in dirs:
                dfs(x + dx, y + dy)

        # Find first island and mark it
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # Step 2: BFS to expand the first island until we reach the second island
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny]:
                            if grid[nx][ny] == 1:
                                return steps  # Reached second island
                            elif grid[nx][ny] == 0:
                                visited[nx][ny] = True
                                grid[nx][ny] = 2
                                q.append((nx, ny))
            steps += 1

        return -1  # Should never reach here
