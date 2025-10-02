# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        n = len(arr)

        for i in range(n-1, -1, -1):
            curr = arr[i]

            arr[i] = maxRight

            maxRight = max(maxRight, curr)
        return arr

       
        