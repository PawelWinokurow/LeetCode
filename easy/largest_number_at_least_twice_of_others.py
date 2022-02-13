from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_ = max(nums)
        idx = nums.index(max_)
        nums.pop(idx)
        return idx if max_ - 2 * max(nums) >= 0 else -1