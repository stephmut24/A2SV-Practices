# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char_count = [0, 0, 0]
        for right in range(len(s)):
            char_count[ord(s[right]) - ord('a')] += 1

            while char_count[0] > 0 and char_count[1] > 0 and char_count[2] > 0:
                char_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            count += left
        return count