# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                temp, idx = stack.pop()
                ans[idx] = i - idx
            
            stack.append([t, i])
        
        return ans