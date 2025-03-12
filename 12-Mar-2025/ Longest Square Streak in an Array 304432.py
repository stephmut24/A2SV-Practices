# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums.sort()
        max_streak = -1

        for num in nums:
            current_streak = 0
            current_num = num

            while current_num in num_set:
                current_streak +=1
                current_num *= current_num
            if current_streak >=2:
                max_streak =max(max_streak, current_streak)
        return max_streak

        