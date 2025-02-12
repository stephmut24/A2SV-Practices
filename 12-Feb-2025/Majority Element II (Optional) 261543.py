# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2=0, 0
        candidate1, candidate2 = None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -=1 
                count2 -=1

        result =[]
                
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)
        return result

    
        