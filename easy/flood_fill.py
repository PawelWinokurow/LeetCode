from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if not(0 <= row < rows and 0 <= col < cols and image[row][col] == orig_color):
                return
            image[row][col] = newColor
            for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                traverse(row + x, col + y)
        if orig_color != newColor:
            traverse(sr, sc)

        return image



