ans = []
for _ in range(int(input())):
    while True:
        R = input()
        if R != '':
            R = int(R)
            break
    L = 0
    lk = []
    lv = []
    while True:
        get = input()
        if get == '0 0':
            break
        n1, n2 = map(int, get.split())
        lk.append(n1)
        lv.append(n2)
    chose = []
    con = False
    while L < R:
        l = []
        l_ind = []
        for i in range(len(lk)):
            if lk[i] <= L:
                l.append(lv[i])
                l_ind.append(i)
        if len(l)==0 or l_ind[l.index(max(l))] in chose:
            con = True
            break
        else:
            chose.append(l_ind[l.index(max(l))])
            L = lv[l_ind[l.index(max(l))]]
    if con:
        ans.append(0)
    else:
        ans.append(len(chose))
        for x in chose:
            ans.append(f"{lk[x]} {lv[x]}")
    ans.append('')
[print(x)for x in ans[:-1]]