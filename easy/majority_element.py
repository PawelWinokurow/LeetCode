from typing import List


class Solution:
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate


nums = [2,2,1,1,1,2,2]
sol = Solution()
ret = sol.majorityElement(nums)
pass