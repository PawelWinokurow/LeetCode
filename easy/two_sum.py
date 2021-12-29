from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in d:
                return [d[num_to_find], i]
            d[nums[i]] = i