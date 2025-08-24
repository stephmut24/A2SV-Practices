# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        from functools import reduce
        x = reduce(lambda a, b: a ^ b, nums, 0)
        y = x & -x
        return [
            reduce(lambda a, b: a ^ b, filter(lambda n: n & y, nums), 0),
            reduce(lambda a, b: a ^ b, filter(lambda n: not n & y, nums), 0)
        ]