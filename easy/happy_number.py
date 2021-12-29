class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n not in mem:
            mem.add(n)
            n = sum([int(ch) ** 2 for ch in str(n)])
        return n == 1
