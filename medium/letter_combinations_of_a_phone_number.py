import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        d = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j","k","l"], "6": ["m","n","o"], "7": ["p","q","r","s"], "8": ["t","u","v"], "9": ["w","x","y","z"]}
        return ["".join(t) for t in itertools.product(*[d[c] for c in digits])]
