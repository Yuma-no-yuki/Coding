ans = []
for __ in range(int(input())):
    ans.append('')
    l = []
    for _ in range(int(input())):
        n1,n2,n3 = input().split(' ')
        l.append([n1,int(n2),int(n3)])
    check = []
    for _ in range(int(input())):
        check.append(int(input()))
    for i in check:
        m = []
        count = 0
        for x in range(len(l)):
            if l[x][1] <= i and i <= l[x][2]:
                m.append(l[x][0])
        if len(m) == 1:
            ans.append(m[0])
        else:
            ans.append('UNDETERMINED')
[print(x)for x in ans[1:]]