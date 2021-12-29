from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0:
            if j >= 0 and (i < 0 or nums1[i] <= nums2[j]):
                nums1[k] = nums2[j]
                j -= 1
            elif i >= 0 and (j < 0 or nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            k -= 1