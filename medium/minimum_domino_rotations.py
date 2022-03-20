from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check_row(el, first_row, second_row):
            count = 0
            for i in range(len(first_row)):
                if first_row[i] != el:
                    if second_row[i] != el:
                        count = -1
                        break
                    else:
                        count += 1
            return count

        ans = {check_row(tops[0], tops, bottoms), check_row(bottoms[0], tops, bottoms),
               check_row(bottoms[0], bottoms, tops), check_row(tops[0], bottoms, tops)}
        if -1 in ans:
            ans.remove(-1)
        if not ans:
            return -1
        else:
            return min(ans)