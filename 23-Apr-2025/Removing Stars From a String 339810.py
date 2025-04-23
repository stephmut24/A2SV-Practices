# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans += [i]
        return "".join(ans)