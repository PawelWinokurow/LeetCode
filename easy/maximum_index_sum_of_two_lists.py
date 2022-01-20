from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i, item in enumerate(list1):
            d[item] = [i, float('inf')]
        for i, item in enumerate(list2):
            if item in d:
                d[item][1] = i
            else:
                d[item] = [float('inf'), i]
        ans = sorted(d.values(), key=lambda x: sum(x))
        return list(map(list1.__getitem__, map(lambda x: x[0], filter(lambda x: sum(x) == sum(ans[0]), ans))))


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
sol = Solution()
ret = sol.findRestaurant(list1, list2)
pass