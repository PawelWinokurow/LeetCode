class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return len(set(zip(pattern, words))) == len(set(words)) == len(set(pattern)) and len(words) == len(pattern)

