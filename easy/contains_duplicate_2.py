from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, v in enumerate(nums):
            if v in d and d[nums[i]] >= i - k:
                return True
            d[nums[i]] = i
        return False