ans=[]
try:
    while True:
        x = input()
        if x !="":
            x=int(x)
        l = [int(num)for num in input().split(" ") if num !=""]
        lt = [int(num)for num in range(len(l))][::-1]
        if x == 0:
            if len(l)>=2:
                ans.append(l[-2])
            else:
                ans.append(0)
            continue
        cal = 0
        for i in range(len(l)):
            cal += l[i]*lt[i]*(x**(lt[i]-1))
        ans.append(int(cal))
except EOFError:
    pass
[print(x)for x in ans]