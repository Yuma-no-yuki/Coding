#須改combin的排序
ans=[]
cc=0
try:
    while True:
        cc+=1
        a = int(input())
        b = a
        s=f'{cc}. '
        if a<100:
            s+=str(a)
        else:
            l=['kuti','lakh','hajar','shata']
            l2=[10000000,100000,1000,100] #7 5 3 2
            count=[0,0,0,0]
            combin=[]
            while a>=100:
                for i in range(len(l2)):
                    if a>i:
                        count[i]=a//l2[i]
                        a=a-(a//l2[i])*l2[i]
                if count[0]<100:
                    [combin.append(x) for x in count]
                    if a!=0:
                        combin.append(a)
                else:
                    [combin.append(x)for x in count[1:]]
                    if a!=0:
                        combin.append(a)
                a=count[0]
            c1=combin[4:-1]
            c2=combin[0:3]
            c2.insert(0,combin[-1])
            if c1 ==[]:
                c2=combin[0:-1]
            for i in range(len(c1)):
                if c1[i]!=0:
                    s+=f"{c1[i]} {l[i]} "
            for i in range(len(c2)):
                if c2[i]==0 and i==0 and b>10000000:
                    s+=f"{l[i]} "
                elif c2[i]!=0:
                    s+=f"{c2[i]} {l[i]} "
            if c1 == []:
                s+=str(combin[-1])
            elif combin[3]!=0:
                s+=str(combin[3])
        ans.append(s)
except EOFError:
    pass
[print(_)for _ in ans]
