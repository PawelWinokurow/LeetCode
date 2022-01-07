from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num += grid[i][j] * (4 - (grid[i][j-1] if j > 0 else 0) - (grid[i-1][j] if i > 0 else 0) - (grid[i][j+1] if j < len(grid[0])-1 else 0) - (grid[i+1][j] if i < len(grid)-1 else 0))
        return num
