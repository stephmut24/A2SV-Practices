# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Directions allowed for each street type (1 to 6)
        directions = {
            1: [(0, -1), (0, 1)],      # Left, Right
            2: [(-1, 0), (1, 0)],      # Up, Down
            3: [(0, -1), (1, 0)],      # Left, Down
            4: [(0, 1), (1, 0)],       # Right, Down
            5: [(0, -1), (-1, 0)],     # Left, Up
            6: [(0, 1), (-1, 0)]       # Right, Up
        }

        visited = set([(0, 0)])  # Track visited cells
        destination = (len(grid) - 1, len(grid[0]) - 1)

        def inbound(row, col):
            # Check if coordinates are within grid bounds
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            # Base case: reached the destination
            if (row, col) == destination:
                return True

            # Explore all allowed directions from the current cell
            for row_change, col_change in directions[grid[row][col]]:
                new_row = row + row_change
                new_col = col + col_change

                # Move if:
                # 1. next cell is in bounds
                # 2. not visited
                # 3. the next cell has a connection back to the current cell
                if (
                    inbound(new_row, new_col)
                    and (new_row, new_col) not in visited
                    and (-row_change, -col_change) in directions[grid[new_row][new_col]]
                ):
                    visited.add((new_row, new_col))
                    if dfs(new_row, new_col):
                        return True

            return False  # No valid path found from current cell

        return dfs(0, 0)  # Start DFS from top-left corner

            