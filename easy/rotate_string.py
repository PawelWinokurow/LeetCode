class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        idx = (s + s).find(goal)
        return s[idx:] + s[:idx] == goal

