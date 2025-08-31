# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def cirno(x):
    if x == 1:
        return 3
    elif x & (x - 1) == 0:
        return x + 1
    else:
        return x & -x
t = int(input())

for _ in range(t):
    x = int(input())
    print(cirno(x))