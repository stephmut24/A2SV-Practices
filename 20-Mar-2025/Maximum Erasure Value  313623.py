# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        set_list= set()
        
        l, res, total = 0, 0, 0

        for r in range(len(nums)):
            
            while nums[r] in set_list:
                set_list.remove(nums[l])
                total -= nums[l]
                l += 1

            set_list.add(nums[r])
            total += nums[r]
            res = max(res, total)
        return res