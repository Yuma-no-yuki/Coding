#DP
m=int(input())
coin=[1,5,10,25,50]
c=[0]*7490
c[0]=1
for i in range(len(coin)):
    for j in range(coin[i],int(m)+1):
        c[j]+=c[j-coin[i]]
        print(f"c[{j}]+=c[{j-coin[i]}],i={i},j={j}")
print(c[int(m)])
