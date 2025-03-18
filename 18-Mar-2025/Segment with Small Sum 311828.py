# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
cur_sum = 0
maxL = 0

for r in range(n):
    cur_sum += a[r]

    while cur_sum > s:
        cur_sum -= a[l]
        l +=1

    maxL = max(maxL, r - l + 1)

print(maxL)