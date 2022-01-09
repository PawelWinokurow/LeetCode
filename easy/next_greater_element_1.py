from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            start_i = nums2.index(n)
            a = -1
            for i in range(start_i + 1, len(nums2)):
                if nums2[i] > nums2[start_i]:
                    a = nums2[i]
                    break
            ans.append(a)
        return ans