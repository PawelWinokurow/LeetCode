from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def get_count(h, w, r, c):
            y_0, y_1 = max(r - 1, 0), min(r + 2, h)
            x_0, x_1 = max(c - 1, 0), min(c + 2, w)
            return (y_1 - y_0) * (x_1 - x_0)

        ans = [[0] * len(r) for r in img]

        img = [[0] * len(img[0])] + img + [[0] * len(img[0])]
        for r in range(len(img)):
            img[r] = [0] + img[r] + [0]
        for r in range(1, len(img)-1):
            for c in range(1, len(img[0])-1):
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        ans[r-1][c-1] += img[i][j]
                ans[r-1][c-1] = int(ans[r-1][c-1] / get_count(len(ans), len(ans[0]), r-1, c-1))
        return ans
