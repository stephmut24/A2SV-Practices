# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prifix_sum = [0]*(len(s) + 1)


        for start,end,dirc in shifts:
            # move backward
            if dirc == 0:
                prifix_sum[start] -= 1
                prifix_sum[end + 1] += 1


            # move forward
            else:
                prifix_sum[start] += 1
                prifix_sum[end + 1] -= 1

        # build the prefix summ
        for i in range(1,len(s) + 1):
            prifix_sum[i] += prifix_sum[i - 1]

        ans = ""
        for i in range(len(s)):
            ans += chr(((ord(s[i]) + prifix_sum[i] - 97) % 26) + 97)


        return ans