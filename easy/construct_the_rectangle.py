import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = int(math.sqrt(area))
        for l in range(sqrt, area + 1):
            if area % l == 0:
                return [max(l, area // l), min(l, area // l)]
