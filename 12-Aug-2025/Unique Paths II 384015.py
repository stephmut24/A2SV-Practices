# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[n-1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if grid[r][c]:
                    dp[c] = 0
                elif c+1 < n:
                    dp[c] = dp[c] + dp[c+1]
        return dp[0]
          

        