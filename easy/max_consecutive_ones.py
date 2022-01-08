from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                max_ = max(count, max_)
            else:
                count = 0
        return max_
