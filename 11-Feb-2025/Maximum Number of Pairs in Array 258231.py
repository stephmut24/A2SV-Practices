# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count= Counter(nums)
        pairs=0
        leftNum = 0

        for i in count.values():
            pairs += i // 2
            leftNum += i %2

        return [pairs, leftNum]


        