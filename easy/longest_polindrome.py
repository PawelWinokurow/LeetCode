import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        all = 0
        l = 0
        count = collections.Counter(s)
        for i in count.values():
            all += i
            if i % 2 == 0:
                l += i
            else:
                l += i - 1
        return l + 1 if all > l else l