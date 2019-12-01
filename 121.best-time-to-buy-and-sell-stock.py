#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (48.68%)
# Likes:    3479
# Dislikes: 154
# Total Accepted:    648.1K
# Total Submissions: 1.3M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        if len(prices)<=1:
            return p
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]>=prices[i-1]:
                p = max(p,prices[i]-buy)
            else:
                buy = min(prices[i],buy)
        return p
# @lc code=end

