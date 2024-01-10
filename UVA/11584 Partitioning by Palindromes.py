ans=[]
get=int(input())
dp=[0]*10
dp[1]=1
for i in range(get):
    a=input()
    l=[]
    l2=[]
    for i in range(2, len(a)+1):
        dp[i]=dp[i-1]+1
        for j in range(0,i-1):
            if a[i-1]==a[j]:
                dp[i]=min(dp[j]+1,dp[i])
    ans.append(dp[len(a)])
[print(x)for x in ans]
