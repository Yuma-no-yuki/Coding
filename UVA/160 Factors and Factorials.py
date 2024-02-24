l = []
con = 1
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            con = 2
    if con == 1:
        l.append(i)
    con = 1
ans = []
while True:
    get = int(input())
    if get == 0:
        break
    num = [[1]]
    fL = [0] * len(l)
    ll = []
    for ori in range(2,101):
        while ori !=1:
            for x in l:
                if ori%x == 0:
                    fL[l.index(x)]+=1
                    ori = ori // x
        ll.append([str(k) for k in fL if k!=0])
    s = f"{get:3d}! ="
    for t in ['{:>3}'.format(x) for x in ll[get-2][:15]]:
        s += (t)
    ans.append(s)
    if len(ll[get-2])>15:
        s2 = "      "
        for t in ['{:>3}'.format(x) for x in ll[get-2][15:]]:
            s2 += (t)
        ans.append(s2)
[print(x)for x in ans]