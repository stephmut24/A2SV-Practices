# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        x = [""] * n

        for i in range(n):
            x[indices[i]] = s[i]
        return "".join(x)