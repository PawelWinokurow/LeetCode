class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # ord(0) = 48
        s = ''
        zeros = '0' * abs(len(num2) - len(num1))
        long, short = (num2, zeros + num1) if len(num1) < len(num2) else (num1, zeros + num2)
        remainder = 0
        for i in reversed(range(len(long))):
            a = int(short[i]) + int(long[i]) + remainder
            remainder = a // 10
            s = str(a % 10) + s
        if remainder:
            s = '1' + s
        return s