# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        arr_length = len(arr)
        cur_pointer = arr_length - 1

        while cur_pointer >= 0:
            if cur_pointer + zeros < arr_length:
                arr[cur_pointer + zeros] = arr[cur_pointer]
            
            if arr[cur_pointer] == 0 :
                zeros -= 1
                if cur_pointer + zeros < arr_length:
                    arr[cur_pointer + zeros] = 0
                    
            cur_pointer -= 1
        