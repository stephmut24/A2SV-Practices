# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        big, small = [], []

        for num in range(1, int(math.sqrt(n))+1):
            if n % num == 0:
                if num == n // num:
                    small.append(num)
                else:
                    small.append(min(num, n // num))
                    big.append(max(num, n // num))
        big.reverse()
        all_fac = small + big
        if len(all_fac) >=k:
            return all_fac[k-1]
        return -1