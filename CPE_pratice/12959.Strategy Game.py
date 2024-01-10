ans=[]
t=[]
while True:
    get_in=input()
    if get_in == "0 0":
        break
    a=get_in.split(" ")
    get_num=input()
    b=get_num.split(" ")
    b=[int(x) for x in b]
    t.append((max([i for i, x in enumerate(b) if x == max(b)]))%int(a[0]))
    ans.append(t[0]+1)
    t=[]
for i in ans:
    print(i)