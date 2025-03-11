# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        operations = 0
        prev_unique = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev_unique: continue

            if nums[i] < prev_unique:
                operations += i
            prev_unique = nums[i]
        
        return operations