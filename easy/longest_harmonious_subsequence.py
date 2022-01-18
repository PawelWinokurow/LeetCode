from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        candidates = set(nums)
        candidates_ = filter(lambda x: x+1 in candidates, candidates)

        ans = 0
        counter = Counter(nums)
        for n in candidates_:
            ans = max(ans, counter[n] + counter[n+1])
        return ans
