# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_num = 0
        run=[]
        for i in nums:
            curr_num += i
            run.append(curr_num)
        return run


        