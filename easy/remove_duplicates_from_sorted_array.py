from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        i = 0
        while i < len(nums):
            if nums[i] in d:
                del nums[i]
            else:
                d[nums[i]] = True
                i += 1
        return len(nums)