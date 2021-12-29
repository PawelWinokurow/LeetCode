class Solution:
    def titleToNumber(self, columnNumber: int) -> str:
        s = ''
        while columnNumber > 0:
            t = columnNumber % 26 if columnNumber % 26 != 0 else 26
            s = chr(t + 64) + s
            columnNumber = (columnNumber - 1) // 26
        return s
