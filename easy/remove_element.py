from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = list(filter(lambda x: x != val, nums))
        return len(nums)