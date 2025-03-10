# Problem: D - Pirates Island: Painting the Grand Line - https://codeforces.com/gym/594356/problem/D

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    cost = {}

    # first pass: Initialize all colors to 1
    for i in range(n):
        for j in range(m):
            color = grid[i][j]

            cost.setdefault(color, 1)  

    # second pass: Check for adjacent cells of the same color
    for i in range(n):
        for j in range(m):
            color = grid[i][j]

            if (j + 1 < m and grid[i][j + 1] == color) or (i + 1 < n and grid[i + 1][j] == color):
                cost[color] = 2

    total_cost = sum(cost.values())

    # this will be 2 if any color is non-isolated, otherwise 1
    max_cost = max(cost.values())  
    print(total_cost - max_cost)