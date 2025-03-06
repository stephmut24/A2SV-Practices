# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        k = []

        for idx in range(x):
            max_ = max(arr[:x -idx])
            max_idx = arr.index(max_) + 1
            arr[:max_idx] = reversed(arr[:max_idx])
            k.append(max_idx)

            arr[:x - idx] = reversed(arr[:x - idx])

            k.append(x - idx)
        return k
        