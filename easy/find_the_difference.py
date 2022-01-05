import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (collections.Counter(t) - collections.Counter(s)).popitem()[0]