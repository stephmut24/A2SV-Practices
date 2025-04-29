# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}

        for i, char in enumerate(s):
            last_occur[char] = i

        stack = []
        visited = set()

        for i in range(len(s)):
            if s[i] in visited:
                continue

            while stack and s[i] < stack[-1] and i < last_occur.get(stack[-1], -1):
                visited.remove(stack.pop())
            visited.add(s[i])
            stack.append(s[i])

        return ''.join(stack)

        