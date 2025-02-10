# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

import sys

def check_1100(buf, i, n):
   
    return i + 3 < n and buf[i] == '1' and buf[i + 1] == '1' and buf[i + 2] == '0' and buf[i + 3] == '0'

def solve():
    
    buf = list(sys.stdin.readline().strip()) 
    n = len(buf)  

   
    count = sum(1 for i in range(n - 3) if check_1100(buf, i, n))

    q = int(sys.stdin.readline().strip())  
    results = []  

    for _ in range(q):
        i, v = map(int, sys.stdin.readline().split())  
        i -= 1  

        if buf[i] == str(v):  
            
            results.append("YES" if count > 0 else "NO")
            continue  

        
        before = sum(1 for j in range(max(0, i - 3), min(n - 3, i + 1)) if check_1100(buf, j, n))

        
        buf[i] = str(v)

        
        after = sum(1 for j in range(max(0, i - 3), min(n - 3, i + 1)) if check_1100(buf, j, n))

        
        count += after - before

        
        results.append("YES" if count > 0 else "NO")

    
    sys.stdout.write("\n".join(results) + "\n")


t = int(sys.stdin.readline().strip())

for _ in range(t):
    solve()
