# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1 = [(i, j) for i, row in enumerate(img1) for j, item in enumerate(row) if item]
        img2 = [(i, j) for i, row in enumerate(img2) for j, item in enumerate(row) if item]
        count = collections.Counter((ax-bx, ay-by) for ax, ay in img1 for bx, by in img2)
        return max(count.values() or [0])