class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x // 2 + 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high