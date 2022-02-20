from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_area(p1, p2, p3):
            return 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1])
        areas = []
        for i in range(len(points)):
            for j in range(1, len(points)):
                for k in range(2, len(points)):
                    areas.append(get_area(points[i], points[j], points[k]))
        return max(areas)




