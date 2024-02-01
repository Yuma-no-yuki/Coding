#k=4 h=6
#5+4+3+2=14
ans=[]
for i in range(int(input())):
    k,h=map(int,input().split(" "))
    ans.append(int(((h-1)+(h-k))*k/2))
[print(x)for x in ans]
