ans=[]
while True:
    a=int(input())
    if a==0:
        break
    elif a==1 or a==2:
        ans.append(0)
    else:
        DP=[
            [1,1,0,0], #[層數][幾個U排一起(p.s看後面部分)] #第一層可放U或L
            [2,1,1,0],
            [4,2,1,1]  #有3個以上U排(危險排列)一起時都存最後一個陣列 <[n][3]>
            #可推出第四層為[7, 4, 2, 3]
            #7=上一層[4,2,1,1]->0+1+2(index位置)(p.s:在最後面接L,後面沒U)
            #4=上一層[4,2,1,1]->0(index位置)(p.s後面只能有一個U)
            #2=上一層[4,2,1,1]->1(index位置)(p.s後面有兩個U)
            #3=上一層[4,2,1,1]->2+3*2(index位置)(p.s後面有三個U,3*2是因為可以接U或L)
        ]
        for i in range(3,a):
            DP.append([DP[i-1][0] + DP[i-1][1] + DP[i-1][2],DP[i-1][0],DP[i-1][1],DP[i-1][2] + DP[i-1][3]*2])
        ans.append(DP[-1][-1])
[print(x)for x in ans]