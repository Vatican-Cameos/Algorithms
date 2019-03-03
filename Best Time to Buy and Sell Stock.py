#Say you have an array for which the ith element is the price of a given stock #on day i.

#If you were only permitted to complete at most one transaction (i.e., buy one #and sell one share of the stock), design an algorithm to find the maximum #profit.

#Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP - Recurrence Relation : opt(i) = Max(opt(i-1), prices[i] - prices[buydate]). if prices[buydate] > prices[i] : then we have reached the max of profit for that buydate we can do better with ith buy date
        size = len(prices)
        result = [None] * (size + 1)
        
        result[0] = 0
        buyDate = 0
        for i in range(1,size):
            result[i] = max(result[i-1], prices[i] - prices[buyDate])
            if(prices[buyDate] > prices[i]):
                buyDate = i
        return result[size-1]  
