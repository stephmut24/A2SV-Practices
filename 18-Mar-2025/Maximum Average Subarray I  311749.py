# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_Sum = sum(nums[:k])
        cur_sum = max_Sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]  
            max_Sum = max(max_Sum, cur_sum)

        return max_Sum /k
        