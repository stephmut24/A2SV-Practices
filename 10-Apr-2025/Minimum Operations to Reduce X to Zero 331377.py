# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ans = 10 ** 10
        rpref = [0] * len(nums)
        rpref[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            rpref[i] = nums[i] + rpref[i+1]

        lsum = 0
        r = len(nums) - 1
        while r > 0 and rpref[r] < x:
            r -= 1

 
        if rpref[r] == x:
            ans = len(nums) - r
        print(r)
        for l in range(len(nums)):
            lsum += nums[l]
            while r < len(nums) and rpref[r] > x - lsum:
                r += 1

            if lsum == x:
                ans = min(ans, l + 1)
            if r < len(nums) and rpref[r] == x - lsum and r > l: 
                ans = min(ans, l + 1 + (len(nums) -r))

        if ans == 10 ** 10:
            return(-1)
        else:
            return(ans)
                