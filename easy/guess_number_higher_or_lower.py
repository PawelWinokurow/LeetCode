class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        mid = (low + high) // 2
        while low <= high:
            if not guess(mid):
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
