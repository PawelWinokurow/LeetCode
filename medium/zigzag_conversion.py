class Solution:
    def convert(self, text: str, numRows: int) -> str:
        if numRows < 2:
            return text
        strings = ['' for i in range(numRows)]
        op = 1
        cur_row = 0
        for i, c in enumerate(text):
            strings[cur_row] += c

            cur_row += op

            if cur_row == 0 or cur_row == numRows-1:
                if cur_row == 0:
                    op = 1
                else:
                    op = -1
        output = ''.join(strings)
        return output