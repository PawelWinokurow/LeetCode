class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        hex = ''
        for _ in range(8):
            hex = '0123456789abcdef'[num & 15] + hex
            num = num >> 4
        return hex.strip('0')