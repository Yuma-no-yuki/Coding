class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0 #買入時機
        r=1 #賣出時機
        topP = 0
        while r < len((prices)):
            if prices[r] > prices[l]:
                currentP = prices[r] - prices[l]
                topP = max(currentP,topP)
                print(currentP,prices[l],prices[r])
            else:
                l = r
            r+=1

Solution().maxProfit([7,1,5,3,6,4])