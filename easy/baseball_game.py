from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = 0
        arr = []
        for op in ops:
            if op.isnumeric() or op.startswith('-'):
                arr.append(int(op))
                ans += arr[-1]
            elif op == 'C':
                ans -= arr[-1]
                arr.pop()
            elif op == 'D':
                arr.append(arr[-1] * 2)
                ans += arr[-1]
            elif op == '+':
                arr.append(arr[-2] + arr[-1])
                ans += arr[-1]
        return ans