# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q= len(nums)
        for i,c in enumerate (nums):
            nums[i] +=q *(nums[c] % q)
        
        for i, _ in enumerate(nums):
            nums[i] //=q
        return nums
        