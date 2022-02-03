from collections import Counter
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_rev = nums[::-1]
        counter = Counter(nums)
        max_ = max(counter, key=counter.get)
        max_value = counter[max_]
        t = set()
        while counter[max(counter, key=counter.get)] == max_value:
            fst = nums.index(max_)
            snd = len(nums) - 1 - nums_rev.index(max_)
            t.add(snd - fst + 1)
            counter[max_] = 0
            max_ = max(counter, key=counter.get)
        return min(t)
