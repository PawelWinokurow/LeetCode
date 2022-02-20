from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lens = {chr(i+97): l for i, l in enumerate(widths)}
        num_lines = 1
        remains = 100
        for ch in s:
            if remains - lens[ch] >= 0:
                remains -= lens[ch]
            else:
                num_lines += 1
                remains = 100 - lens[ch]
        return [num_lines, 100 - remains]

