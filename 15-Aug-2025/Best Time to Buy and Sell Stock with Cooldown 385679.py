# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dp(index, bought):
            if index >= len(prices):
                return 0

            state = (index, bought)
            if state in cache:
                return cache[state]

            
            leave = dp(index + 1, bought)

            if bought:
                
                sell = prices[index] + dp(index + 2, False)
                cache[state] = max(leave, sell)
            else:
                
                buy = -prices[index] + dp(index + 1, True)
                cache[state] = max(leave, buy)

            return cache[state]

        return dp(0, False)
