from math import sqrt


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num > 1:
                for i in range(2, int(sqrt(num)) + 1):
                    if (num % i) == 0:
                        return False
                else:
                    return True
            else:
                return False
        count = 0
        for n in range(left, right+1):
            count += 1 if is_prime(bin(n).count('1')) else 0
        return count



left = 6
right = 10

sol = Solution()
ret = sol.countPrimeSetBits(left, right)
assert ret == 4