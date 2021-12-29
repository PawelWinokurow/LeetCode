class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        result = ''
        if len_a < len_b:
            a = '0' * (len_b-len_a) + a
        else:
            b = '0' * (len_a-len_b) + b
        remainder = 0
        for i in range(len(a)):
            sum = int(a[-i-1]) + int(b[-i-1])
            result = str((sum + remainder) % 2) + result
            remainder = (sum + remainder) // 2
        if remainder:
            result = '1' + result
        return result