# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
fr = []

for _ in range(n):
    money, friendship = map(int, input().split())
    fr.append((money, friendship))

fr.sort()

l = 0
curr_frindship = 0
max_friendship = 0

for r in range(n):
    curr_frindship += fr[r][1]

    while fr[r][0] - fr[l][0] >= d:
        curr_frindship -= fr[l][1]
        l += 1

    max_friendship = max(max_friendship, curr_frindship)

print(max_friendship)