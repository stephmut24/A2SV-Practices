# Problem: C - The Double-Holed Culprit - https://codeforces.com/gym/622136/problem/C

def find_culprits(n, p):
    result = []

    for start in range(1, n + 1):
        visited = set()
        current = start

        while current not in visited:
            visited.add(current)
            current = p[current - 1]  

        result.append(current)

    return result



n = int(input())
p = list(map(int, input().split()))



culprits = find_culprits(n, p)


print(' '.join(map(str, culprits)))
