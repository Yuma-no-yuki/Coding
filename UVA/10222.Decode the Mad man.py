times=int(input())
ansall=[]
for do in range(times):
    l=["1234567890-=","qwertyuiop[]","asdfghjkl;'","zxcvbnm,./"]
    ans=[]
    b=input()
    b=b.replace("I","i")
    a=list(b)
    for i in a:
        if i==" ":
            ans.append(" ")
        for j in range(len(l)):
            for t in range(len(l[j])):
                if i==l[j][t]:
                    ans.append(l[j][t-2])
                else:
                    continue
    ansall.append(''.join(ans))
for get in ansall:
    print(get)