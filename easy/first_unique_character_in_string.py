import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_ = []
        for k, v in collections.Counter(s).items():
            if v == 1:
                s_.append(k)
        return min(map(s.find, s_)) if len(s_) else -1
