# Problem: 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        s_set = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l +=1
            s_set.add(s[r])
            max_length = max(max_length,  r - l + 1)
        
        return max_length

        
        