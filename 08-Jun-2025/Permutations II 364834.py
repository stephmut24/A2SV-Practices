# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations =[]
        counter = Counter(nums)

        def FindAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    FindAllPermutations(res + [key])
                    counter[key] += 1

        FindAllPermutations([])
        return permutations