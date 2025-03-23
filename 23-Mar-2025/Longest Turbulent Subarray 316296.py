# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, 0
        ans = 1
        if n == 1:
            return 1

        while r < n:
            while l < n - 1 and arr[l] == arr[l+1]: 
                l += 1
            while r < n - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            ans=max(ans, r - l + 1)
            l = r
            r += 1
        return ans
        