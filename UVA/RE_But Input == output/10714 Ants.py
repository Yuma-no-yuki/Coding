ans = []
for _ in range(int(input())):
    n1,n2 = map(int,input().split(' '))
    m=0
    M=0
    l = [int(x)for x in input().split(' ') if x != '']
    for i in range(n2):
        d1,d2 = n1-l[i],l[i]
        if d1<d2:
            d1,d2=d2,d1
        if M < d1:
            M = d1
        if m < d2:
            m = d2
    ans.append(f"{m} {M}")
[print(x)for x in ans]