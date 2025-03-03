# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

mat = []

for _ in range(5):
    mat.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if mat[i][j] ==1:
            print(abs(2-i)+abs(2-j))
            exit()