# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards=list(map(int, input().split()))
l = 0
r= n - 1
ser = 0
di = 0
turn = 0
while l <= r:
    if cards[l] > cards[r]:
        chosen = cards[l]
        l += 1
    else:
        chosen = cards[r]
        r -= 1
    if turn % 2 == 0:
        ser += chosen
    else:
        di += chosen
    turn += 1
print(ser, di)

