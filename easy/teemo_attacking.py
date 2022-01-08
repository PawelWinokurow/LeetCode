from functools import reduce
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = [[0,0]]
        for t in timeSeries:
            if ans[-1][1] >= t:
                ans[-1][1] = t + duration
            else:
                ans.append([t, t + duration])
        while ans[0] == [0, 0]:
            ans.pop(0)
        return sum(map(lambda x: x[1] - x[0], ans))
