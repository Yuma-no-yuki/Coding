a=int(input())
b={}
ans=[]
for i in range(a):
    t=input()
    t2=input()
    b.update({t:t2})
a2=int(input())
for i in range(a2):
    t3=input()
    if (t3 in b) == True:
        ans.append(b[t3])
for i in ans:
    print(i)


