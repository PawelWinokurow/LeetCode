class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        mid = int((low + high) // 2)
        while low <= high:
            if mid * mid > num:
                high = mid - 1
            elif mid * mid < num:
                low = mid + 1
            else:
                return True
            mid = int((low + high) // 2)
        return False