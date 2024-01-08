class Solution(object):
    def fib(self, n):
        dp=[0,1]
        c_n = n+1
        if c_n>=2:
            for i in range(2,c_n):
                dp.append(dp[i-2]+dp[i-1])
        return dp[n]
