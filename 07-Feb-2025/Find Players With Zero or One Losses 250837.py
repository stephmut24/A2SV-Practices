# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers= {}

        for match in matches:
            winner, loser = match
            winners.add(winner)
            if loser in losers:
                losers[loser] +=1
            else: 
                losers[loser]=1

        Players_winners= [winner for winner in winners if winner not in losers]
        Players_losers = [loser for loser, count in losers.items() if count ==1]

        return[sorted(Players_winners), sorted(Players_losers)]

        