from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum([1 for t in grid for n in t if n != 0])
        xz = sum([max(t) for t in grid])
        yz = sum([max(t) for t in list(map(list, zip(*grid)))])
        return xy + xz + yz


grid = [[1,0],[0,2]]
sol = Solution()
ret = sol.projectionArea(grid)
assert ret == 8
