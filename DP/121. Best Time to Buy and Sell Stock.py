class Solution(object):
    def maxProfit(self, prices):
        l=0 #買入時機
        r=1 #賣出時機
        topP = 0
        while r < len((prices)):
            if prices[r] > prices[l]:
                currentP = prices[r] - prices[l]
                topP = max(currentP,topP)
            else:#若有比買入時機更低的數值時 EX：當 prices=[7,1,6,0,9]
                l = r 
            r+=1
        return topP
        
