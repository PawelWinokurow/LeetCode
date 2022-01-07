from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans