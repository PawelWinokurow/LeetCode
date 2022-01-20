from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su = sum(nums[:k])
        m = su
        for i in range(1, len(nums) - k + 1):
            su += (nums[i+k-1] - nums[i-1])
            if su > m:
                m = su
        return m/k