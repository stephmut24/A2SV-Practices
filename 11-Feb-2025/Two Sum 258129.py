# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map={}
        num_target= target

        for i,num in enumerate(nums):
            comp= target - num
            if comp in comp_map :
                return[comp_map[comp],i]
            comp_map[num] =i



        