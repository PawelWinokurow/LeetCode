class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = 0
        i = 1
        while n:
            if n & 1:
                if last_pos:
                    max_gap = max(max_gap, i - last_pos)
                last_pos = i
            i += 1
            n >>= 1
        return max_gap