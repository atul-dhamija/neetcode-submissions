class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in prices[i:]:
                
                temp = j - prices[i]
                if (temp > profit):
                    profit = temp
        return profit