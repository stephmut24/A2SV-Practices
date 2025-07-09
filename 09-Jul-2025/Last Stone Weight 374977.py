# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def largest_stone():
            stone_idx = stones.index(max(stones))
            return stones.pop(stone_idx)
        
        while len(stones) > 1:
            x = largest_stone()
            y = largest_stone()
            if x-y:
                stones.append(x-y)
        
        return stones[0] if len(stones) > 0 else 0