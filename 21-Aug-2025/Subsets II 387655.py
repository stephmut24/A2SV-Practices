# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        seen = set()

        for i in range(1 << n):
            subset = []

            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            t = tuple(subset)
            if t not in seen:
                seen.add(t)
                ans.append(subset)
        return ans

        