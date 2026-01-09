123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.


Code:
class Solution(object):
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1=sell2=0
        for price in prices:
            sell2=max(sell2,buy2+price)
            buy2=max(buy2,sell1-price)
            sell1=max(sell1,buy1+price)
            buy1=max(buy1,-price) 
        return sell2       

My Solution:

Four State Variables Approach:
buy1 = Max profit with first stock bought (negative initial cost)

text
buy1 = max(buy1, -price)
sell1 = Max profit after first stock sold

text
sell1 = max(sell1, buy1 + price)
buy2 = Max profit with second stock bought (using profit from first sale)

text
buy2 = max(buy2, sell1 - price)
sell2 = Max profit after second stock sold (final answer)

text
sell2 = max(sell2, buy2 + price)
Key Insights:
Sequential processing - each price updates all four states

Reuse profits - profit from first sale funds second purchase

Track best decisions at each price point

Time complexity: O(n), Space complexity: O(1)


  
