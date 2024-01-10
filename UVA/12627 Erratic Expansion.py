step=int(input())
ans_final=[]
for o in range(step):
    get_in=input()
    k=get_in.split(" ")
    in_num=int(k[0])
    a = [1]
    if int(k[0])==0:
        ans_final.append(1)
    else:
        while in_num!=0:
            c=a+a
            for i in range(len(a)):
                c[i]+=a[i]
            a=c
            in_num-=1
        ans=sum(a[int(k[1])-1:int(k[2])])
        ans_final.append(ans)
for i in range(len(ans_final)):
    print(f"Case {i+1}: {ans_final[i]}")