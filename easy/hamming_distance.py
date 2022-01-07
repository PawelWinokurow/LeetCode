class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = 0
        a = x ^ y
        while a > 0:
            num += a & 1
            a >>= 1
        return num