# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i, j = 0, len(piles) - 1
        total = 0

        while i < j:
            total += piles[j - 1]
            i +=1
            j -=2
        return total

        