# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_length = len(strs[0])
        if len(strs) == 1:
            return strs[0]

        for i in range(strs_length):
            for_check = strs[0][:(strs_length-i)]
            is_good = all(s.startswith(for_check) for s in strs)
            if is_good:
                return for_check
        return ""


        