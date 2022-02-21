from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        horizontal_overlap = (min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])) > 0
        vertical_overlap = (min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])) > 0
        return horizontal_overlap and vertical_overlap