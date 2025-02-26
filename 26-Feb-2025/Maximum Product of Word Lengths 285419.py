# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result=0
        masks = []
        for word in words:
            mask = 0
            for c in word:
                bit =  ord(c) - ord('a')
                mask |= 1<<bit
            masks.append(mask)
        n = len(words)

        for i in range(n):
            for j in range(n):
                if i != j:
                    if masks[i] & masks[j] ==0:
                        result = max(result, len(words[i])* len(words[j]))
        return result

        