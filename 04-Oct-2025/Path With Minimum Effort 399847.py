# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dist_map = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
        dist_map[(0, 0)] = 0
        visited = set()
        visited.add((0,0))
        heap = []
        heapq.heappush(heap, (0, (0, 0)))
        while heap:
            dist, (i, j) = heapq.heappop(heap)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    temp = max(dist, abs(heights[i][j] - heights[ni][nj]))
                    if temp < dist_map[(ni, nj)]:
                        dist_map[(ni, nj)] = temp
                        heapq.heappush(heap, (temp, (ni, nj)))
                        visited.add((i,j))

        return dist_map[(rows-1,cols-1)]