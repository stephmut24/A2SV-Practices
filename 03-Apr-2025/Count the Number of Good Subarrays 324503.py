# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        window_pairs = 0
        count = collections.Counter()
        n = len(nums)
        res = 0
        j = 0
        for i in range(n):
            while j < n and window_pairs < k:
                count[nums[j]] +=1
                window_pairs += count[nums[j]] - 1
                j += 1
            if window_pairs >= k:
                res += n - j + 1
            else:
                break
            count[nums[i]] -= 1
            window_pairs -= count[nums[i]]
        return res 
