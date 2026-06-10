class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=-float("inf")
        minprice=float("inf")
        for i in range(len(prices)):
            minprice = min(prices[i],minprice)
            profit=prices[i]-minprice
            maxprofit=max(profit , maxprofit)
        return maxprofit