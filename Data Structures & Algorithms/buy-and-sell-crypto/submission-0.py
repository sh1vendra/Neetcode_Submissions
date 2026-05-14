class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        l=0
        for r in range(1,len(prices)):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxp= max(maxp,profit)

            else:
                l=r
        return maxp