from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_buy = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - cur_buy)
            cur_buy = min(cur_buy, prices[i])
        return profit

prices = [7,1,5,3,6,4]

sol = Solution()
a = sol.maxProfit(prices)
pass