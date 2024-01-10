class Solution(object):
    def countBits(self, n):
        dp=[0]
        l = dp
        if n==0:
            return dp
        else:
            for i in range(17):
                for j in range(len(l)):
                    dp.append(l[j]+1)
            return dp[:n+1]
