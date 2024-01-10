# https://cpe.cse.nsysu.edu.tw/cpe/test_data/2022-03-22
store_data=[]
def way(a1,a2,a3,ch):
    set=[a1,a2,a3]
    set2=ch
    set2_list=list(set2)
    b=[-1,-1,-1]
    r=[-1,-1,0]
    v=[-1,0,-1]
    g=[0,-1,-1]
    m=[-1,0,0]
    y=[0,-1,0]
    c=[0,0,-1]
    w=[0,0,0]
    while True:
        if len(set2_list)==0:
            break
        elif set2_list[0]=="B":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=b[i]
        elif set2_list[0]=="R":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=r[i]
        elif set2_list[0]=="V":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=v[i]
        elif set2_list[0]=="G":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=g[i]
        elif set2_list[0]=="M":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=m[i]
        elif set2_list[0]=="Y":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=y[i]
        elif set2_list[0]=="C":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=c[i]
        elif set2_list[0]=="W":
            set2_list.pop(0)
            for i in range(3):
                set[i]+=w[i]
    if set[0]<0 or set[1]<0 or set[0]<0:
       store_data.append("NO")
    else:
        store_data.append(f"YES {set}")


get=int(input())
for i in range(get):
    a1,a2,a3,a4=map(str,input().split())
    a1=int(a1)
    a2=int(a2)
    a3=int(a3)
    way(a1,a2,a3,a4)
for i in store_data:
    print(i)