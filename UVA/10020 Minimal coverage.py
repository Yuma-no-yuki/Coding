ans = []
for _ in range(int(input())):
    input()
    L = 0
    R = int(input())
    lk = []
    lv = []
    while True:
        get = input()
        if get == '0 0':
            break
        n1,n2 = map(int,get.split(' '))
        lk.append(n1)
        lv.append(n2)
    chose = []
    while L<R:
        l = []
        l_ind = []
        for i in range(len(lk)):
            if lk[i]<L:
                l.append(lv[i])
                l_ind.append(i)
        chose.append(l_ind[l.index(max(l))])
        L = lv[l_ind[l.index(max(l))]]
    ans.append(len(chose))
    for x in chose:
        ans.append(f"{lk[x]} {lv[x]}")
[print(x)for x in ans]