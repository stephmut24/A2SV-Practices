# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n
            stack.append(n)
        for n in stack:
            d[n] = -1
        return [d[x] for x in nums1]

        