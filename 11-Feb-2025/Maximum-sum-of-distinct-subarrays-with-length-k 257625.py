# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res =0
        count =defaultdict(int)
        cur_sum = 0

        l = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            count[nums[i]] +=1

            if i - l +1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] ==0:
                    count.pop(nums[l])
                cur_sum -= nums[l]
                l +=1

            if len(count) == i - l + 1  ==k:
                res = max(res, cur_sum)

        return res
        