from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0, 0)
        digits[-1] = digits[-1] + 1
        for i in range(len(digits)-1):
            if digits[-i-1] == 10:
                digits[-i-1] = 0
                digits[-i-2] += 1

        if digits[0] == 0:
            del digits[0]
        return digits