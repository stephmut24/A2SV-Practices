# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end, L = 0, -1, len(arr)          

        while start < L-1 and arr[start] < arr[start+1]:
            start += 1
        while end > -L and arr[end] < arr[end-1]:
            end -= 1
        return start == end + L and 0 < start and end < -1