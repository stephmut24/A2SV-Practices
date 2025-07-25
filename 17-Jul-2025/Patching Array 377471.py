# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss=1
        patch=0
        i=0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss+=nums[i]
                i+=1
            else:
                patch+=1
                miss+=miss
        return patch
        