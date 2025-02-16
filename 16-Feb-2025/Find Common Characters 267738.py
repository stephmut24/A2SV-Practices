# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq= Counter(words[0])
        for char in words:
            min_freq &=Counter(char)
        return list(min_freq.elements())