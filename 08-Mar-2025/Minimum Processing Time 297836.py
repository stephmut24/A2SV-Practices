# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)

        processorTime.sort()
        tasks.sort(reverse = True)

        mx = 0
        for i in range(n):
            mx = max(mx, processorTime[i] + max(tasks[i*4: i*4+4]))
        return mx
        