L = 0
R = 1
# dic = {-1: 3, -3: 2, 3: 6, 1: 8, 4: 6, 6: 10, 11: 14}
# lk = [-1, -3, 3, 1, 4, 6, 11]
# lv = [3, 2, 6, 8, 6, 10, 14]
# lk = [-1,0]
# lv = [0,1]
lk = [-1,-5,2]
lv = [0,-3,5]
ans = []
chose = []
while L<R:
    l = []
    l_ind = []
    for i in range(len(lk)):
        if lk[i]<=L:
            l.append(lv[i])
            l_ind.append(i)
    chose.append(l_ind[l.index(max(l))])
    L = lv[l_ind[l.index(max(l))]]
    print(L)
for x in chose:
    ans.append(f"{lk[x]} {lv[x]}")
print(ans)