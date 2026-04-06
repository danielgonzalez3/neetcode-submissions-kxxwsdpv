class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 100
        profit = 0

        for n in prices:
            min_p = min(n, min_p)
            profit = max(n - min_p, profit)
    
        return profit

