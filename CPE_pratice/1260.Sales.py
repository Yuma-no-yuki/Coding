count=0
ans=[]
get_in=int(input())
for i in range(get_in):
    num=int(input())
    get_num=input()
    l1=get_num.split(" ")
    l1=[int(x)for x in l1]
    for j in range(1,num):
        for t in range(j):
            if l1[j]>=l1[t]:
                count+=1
    ans.append(count)
    count=0
for i in ans:
    print(i)