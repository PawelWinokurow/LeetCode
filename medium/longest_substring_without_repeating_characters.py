class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def contains_repeats(s):
            return (len(s) - len(set(s))) != 0
        if len(s) == 1:
            return 1
        i = 0
        longest = 0
        for j in range(i+1, len(s)):
            s_ = s[i:j]
            if contains_repeats(s_):
                longest = max(longest, j-1 - i)
                i += s_.index(s[j-1]) + 1
        longest = max(longest, len(s)-1 - i) if contains_repeats(s[i:]) else max(longest, len(s) - i)
        return longest