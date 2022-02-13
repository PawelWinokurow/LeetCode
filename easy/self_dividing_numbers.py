from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sol = []
        for n in range(left, right+1):
            s = str(n)
            if '0' in s:
                continue
            l = list(s)
            if all(map(lambda x: n % int(x) == 0, l)):
                sol.append(n)
        return sol