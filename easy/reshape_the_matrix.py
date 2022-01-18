from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        flat_list = [item for sublist in mat for item in sublist]
        tuples = zip(*([iter(flat_list)] * c))
        return list(map(list, tuples))


mat = [[1,2],[3,4]]
r = 2
c = 2

sol = Solution()
ret = sol.matrixReshape(mat, r, c)
pass
