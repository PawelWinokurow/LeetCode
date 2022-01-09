class Solution:
    def convertToBase7(self, num: int) -> str:
        s = '' if num else '0'
        positive = True if num >= 0 else False
        num = abs(num)
        while num:
            s = str(num % 7) + s
            num //= 7
        return s if positive else '-' + s



num = 0
sol = Solution()
ret = sol.convertToBase7(num)
pass
