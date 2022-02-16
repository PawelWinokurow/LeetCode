from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([w for w in words if not licensePlate - Counter(w)], key=len)

licensePlate = "1s3 PSt"
words = ["step", "steps", "stepss", "stripe", "stepple"]
sol = Solution()
ret = sol.shortestCompletingWord(licensePlate, words)
assert ret == "steps"