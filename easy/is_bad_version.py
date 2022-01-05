class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
        return low
