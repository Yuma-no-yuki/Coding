times=int(input())
ans=[]
for do in range(times):
    a=input()
    a=a.split(" ")
    day=[31,28,31,30,31,30,31,31,30,31,30,31]
    m=int(a[0])
    d=int(a[1])
    day_means=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    calu=0
    for i in range(m-1):
        calu+=day[i]
    calu+=d
    ans.append(day_means[(calu-1)%7])
for get in ans:
    print(get)