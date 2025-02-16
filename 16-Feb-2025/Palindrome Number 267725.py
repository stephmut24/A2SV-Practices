# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        if x < 0 or (x !=0 and x % 10 ==0):
            return False
        
        reversed = 0
        original = x
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x //=10
        return x == reversed or x == reversed // 10