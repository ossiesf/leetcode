# Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Original solution using two pointers to create the sliding window
# Works O(n) but less concise
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        max = 0

        while r < len(prices):
            if prices[r] - prices[l] > max:
                    max = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max

# Updated more concise implementation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Set minPrice to infinity, higher than any price for valid comparisons
        # Setting to 0 keeps minPrice stuck at 0 since min(0, any number) always = 0
        minPrice = float('inf')        
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, (price - minPrice))
        return maxProfit
