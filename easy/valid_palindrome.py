from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for k, v in d.items():
            if v == 1:
                return k
