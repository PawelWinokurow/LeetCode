class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return sum([i for i in range(1, num) if num % i == 0]) == num