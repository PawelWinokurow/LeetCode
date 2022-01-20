from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = 1
        start = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                m = max(m, i - start)
                start = i
        m = max(m, len(nums) - start)
        return m





nums = [1,3,5,4,7]
nums = [2,3, 4]

sol = Solution()
ret = sol.findLengthOfLCIS(nums)
pass