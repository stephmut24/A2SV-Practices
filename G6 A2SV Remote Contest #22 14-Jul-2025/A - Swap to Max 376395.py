# Problem: A - Swap to Max - https://codeforces.com/gym/622136/problem/A

def min_maximum_after_swap(t, text_cases):
    res = []
    
    for case in text_cases:
        n, a,b = case
        
        for i in range(n):
            if a[i] >b[i]:
                a[i], b[i] = b[i],a[i]
                
        max_a = max(a)
        max_b = max(b)
        
        res.append(max_a * max_b)
        
    return res


t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))


res = min_maximum_after_swap(t, test_cases)

for result in res:
    print(result)
    
    