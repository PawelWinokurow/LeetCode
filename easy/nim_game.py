class Solution:

    def canWinNim(self, n: int) -> bool:
        if n < 4:
            return True
        d = [False] * (n+1)
        d[0] = d[1] = d[2] = d[3] = True
        for i in range(4, n+1):
            d[i] = not d[i-1] or not d[i-2] or not d[i-3]
        return d[n]