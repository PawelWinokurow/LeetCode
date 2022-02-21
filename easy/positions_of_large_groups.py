from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        large_groups = []
        start_idx = 0
        cur_c = s[0]
        for i, c in enumerate(s):
            if c != cur_c:
                if i - start_idx >= 3:
                    large_groups.append([start_idx, i-1])
                start_idx = i
                cur_c = c
                continue
        if len(s) - start_idx >= 3:
            large_groups.append([start_idx, len(s)-1])
        return large_groups





s = "aaa"

sol = Solution()
ret = sol.largeGroupPositions(s)
assert ret == [[3,5],[6,9],[12,14]]