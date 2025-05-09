# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = float('inf')

        l = 1
        r = 100000000

        while l <= r:
            c_ans = 0
            mid = l + (r -l) // 2

            for num in nums:
                c_ans += (num + mid -1) // mid

            if c_ans <= threshold:
                ans = min (ans, mid)
                r = mid -1

            else: l = mid +1
        return ans

        