# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        powers = [1] * 10000
        mod = 100000000
        for i in range(1, len(powers)):
            powers[i] = powers[i-1] * 27
            powers[i] %= mod
        def c(char):
            return ord(char) - ord('a') + 1
        def append(val, char):
            return (val * 27 + c(char)) % mod
        def pop(val, char, sz):
            return (val - powers[sz] * c(char)) % mod

        hashvalue = 0
        for char in needle:
            hashvalue = append(hashvalue, char)
        l = 0
        curr_value = 0
        for r in range(len(haystack)):
            curr_value = append(curr_value, haystack[r])
            if r - l + 1 > len(needle):
                curr_value = pop(curr_value, haystack[l], r - l)
                l += 1
            if curr_value == hashvalue:
                return l
        return -1