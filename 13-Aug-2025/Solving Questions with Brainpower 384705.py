# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        for i in range(len(questions) -1, -1, -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1], 0),
                dp.get(i+1,0)
            )
        return dp[0]
           

        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(
                dfs(i+1),
                questions[i][0] + dfs(i+1+ questions[i])
            )

            return dp[i]