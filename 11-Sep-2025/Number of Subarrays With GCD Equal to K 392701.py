# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
 
        def gcd(a, b):
            while a and b:
                a, b = b, a % b
            return a or b
        
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            tmp_gcd = 0 
            
            for j in range(i,n):
                tmp_gcd = gcd(tmp_gcd, nums[j])
                
                if tmp_gcd == k:
                    cnt += 1
                elif tmp_gcd < k:
                    break
        
        return cnt
        
       
  