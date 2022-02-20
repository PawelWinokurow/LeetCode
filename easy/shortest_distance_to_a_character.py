from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = s.find(c)
        idx_next = idx
        ret = []
        for i in range(len(s)):
            diff = abs(idx - i) if abs(idx - i) < abs(idx_next - i) else abs(idx_next - i)
            ret.append(diff)
            if diff == 0 and i + 1 < len(s):
                idx, idx_next = idx_next, i + s[i+1:].find(c) + 1
        return ret