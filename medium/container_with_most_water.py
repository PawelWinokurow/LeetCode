from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_square, width = 0, len(height) - 1, 0, len(height) - 1
        for w in range(width, 0, -1):
            if height[l] < height[r]:
                max_square = max(max_square, w * height[l])
                l += 1
            else:
                max_square = max(max_square, w * height[r])
                r -= 1
        return max_square