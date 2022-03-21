class Solution:
    def reverse(self, x: int) -> int:
        s = ''
        if x < 0:
            s+='-'
            x *= -1
        s += str(x)[::-1]
        if s != '0':
            s = s.lstrip('0')
        x = int(s)
        return 0 if x < -2**31 or x > 2**31 else x