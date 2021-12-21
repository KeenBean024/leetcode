class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Edge Case
        if len(prices)<=1:
            return 0
        
        # Set 2 pointers left and right
        l,r = 0, 1
        max_profit = 0 # Initialize
        
        while r<len(prices):
            
            # if the slope is -ve shift l and r
            if prices[r]-prices[l]<0:
                l=r
                r+=1
            # else continue and update max_profit
            else:
                if prices[r]-prices[l]>max_profit:
                    max_profit = prices[r]-prices[l]
                r+=1
        return max_profit                