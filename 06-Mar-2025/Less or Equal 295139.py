# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C


n, k =map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

if k == 0:
    print(1 if arr[0] > 1 else -1)

else: 
    x = arr[k-1]

    if k < n and arr[k] == x:
        print(-1)
    else:
        print(x)
