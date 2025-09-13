# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        i = 1
        result = []
        while (n>=i):
            if (n % i == 0):
                result.append(n)
            i+=1
        return len(result) == 3