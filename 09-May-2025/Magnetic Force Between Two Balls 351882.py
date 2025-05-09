# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def count(d):
            ans = 1
            pre_pos = position[0]

            for i in range(1, n):
                if position[i] - pre_pos >= d:
                    ans += 1
                    pre_pos = position[i]
            return ans      

        n = len(position)
        position.sort()
        l = 1
        r = position[-1] - position[0]

        while l < r:
            mid = l + (r - l+1)//2

            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l




        