#Problem is 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

  
  
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        minsofar=prices[0]
        total_profit=0
        for i in range(1,len(prices)):
            minsofar=min(minsofar,prices[i])
            total_profit=max(total_profit,prices[i]-minsofar)
        return total_profit        



MY solution :

In order to maximize the profit, we need to minimize the cost price and maximize the selling price. So at every step, we keep track of the minimum buy price of stock encountered so far. For every price, we subtract with the minimum so far and if we get more profit than the current result, we update the result.




