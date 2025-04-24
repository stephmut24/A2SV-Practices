# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char not in pair:
                st.append(char)
            elif not st or st[-1] != pair[char]:
                return False
            else:
                st.pop()
        return len(st) == 0


        