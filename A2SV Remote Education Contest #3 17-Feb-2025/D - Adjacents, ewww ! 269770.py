# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

def construction_matrix():
    
    n = int(input())
    if n == 2 :
        return [[-1]]

    if n == 1:
        return[[1]]
    
    numbers = [[(i + j) % 2, i, j] for i in range(n) for j in range(n)]
    numbers.sort()

    final_matrix = [[0 for i in range(n)] for j in range(n)]

    curr = 1

    for color, i, j in numbers:
        final_matrix[i][j] = curr

        curr += 1

    return final_matrix 

tests = int(input())

for test in range(tests):
    answer = construction_matrix()

    for row in answer:
        print(*row)