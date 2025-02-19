# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        for i in nums:
            if i != 0:
                result.append(i)
        
        diff = len(nums) - len(result)
        result.extend([0] * diff)

        return result
        