from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = [-1] * len(nums)
        for n in nums:
            a[n-1] += 1
        return [a.index(1) + 1, a.index(-1) + 1]
