# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)
        i = 0
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length= len(s)

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0][:i]
            
        