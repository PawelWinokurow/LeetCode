class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        fst = 0 if n & 1 == 1 else 1
        while n:
            if (n ^ fst) & 1 == 0:
                return False
            fst = (fst + 1) % 2
            n >>= 1
        return True
