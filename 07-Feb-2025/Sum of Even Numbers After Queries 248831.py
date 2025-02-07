# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumOfEven = 0
        answer = []
        for ele in nums:
            if (ele%2) == 0:
                sumOfEven += ele
        print(sumOfEven)
        
        for ele, index in queries:
            if abs(nums[index])%2 ==0:
                if abs(nums[index] + ele)%2 ==0:
                    sumOfEven += ele
                else:
                    sumOfEven -= nums[index]

            elif nums[index]%2 !=0 and abs(nums[index]+ ele)%2==0:
                sumOfEven += nums[index]+ele
                
            nums[index] = nums[index]+ele
            answer.append(sumOfEven)
        return answer

        