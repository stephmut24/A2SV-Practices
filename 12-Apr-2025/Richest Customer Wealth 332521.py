# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in range(len(accounts)):
            currentCus = 0
            for j in range(len(accounts[i])):
                currentCus += accounts[i][j]

            res = max(res, currentCus)
               
    
        return res