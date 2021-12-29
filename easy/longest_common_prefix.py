from functools import reduce
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        shortest = strs[0]
        pre = ''
        for i in range(len(shortest)):
            p = shortest[:i+1]
            if reduce(lambda a, s: a and s[:i+1] == p, strs, True):
                pre = p
        return pre