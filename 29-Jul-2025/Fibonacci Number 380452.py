# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    
    def fib(self, n: int) -> int:
        dp = [0]*(n+1)

        def fibb(n):
            if n == 0 or n == 1:
                dp[n] = n
                return n
            if n not in dp:
                dp[n] = fibb( n-1 ) + fibb( n-2 ) 
            
            return dp[n]
        
        return fibb(n)