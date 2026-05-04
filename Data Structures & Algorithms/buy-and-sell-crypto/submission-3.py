class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        min_n = 101
        for n in prices:
            min_n = min(min_n, n)
            delta = n - min_n
            profit = max(profit, delta)
        return profit