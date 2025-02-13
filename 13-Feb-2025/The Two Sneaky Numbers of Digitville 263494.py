# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seenDict = {}
        seen =[]

        for i in nums:
            if i in seenDict:
                seen.append(i)
            else:
                seenDict[i] = 1

        return seen
    

        