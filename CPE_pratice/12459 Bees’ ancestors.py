ans=[]
while True:
    a=int(input())
    if a==0:
        break
    dp=[[0,1]]
    for i in range(1,a):
        dp.append([dp[i-1][1],dp[i-1][0]+dp[i-1][1]])
    ans.append(dp[a-1][0]+dp[a-1][1])
[print(get)for get in ans]