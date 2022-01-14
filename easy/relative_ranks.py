from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        return list(map(dict(zip(score_sorted, rank)).get, score))
