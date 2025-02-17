# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        res=0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if res or (i > 1 and i < len(nums) - 1 and nums[i-2] >nums[i] and nums[i+1] < nums[i-1]):
                    return False
                res = 1
        return True
