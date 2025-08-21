# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            index ^=num
        return index
        