ans = []
while True:
    get = input()
    if get=='0':
        break
    if ' ' in get:
        continue
    l = [0]*int(get)
    con = 0
    for i in range(int(input())):
        n1,n2 = map(int,input().split(' '))
        if l[n1]!=0 and l[n2]!=0 and l[n1]==l[n2]:
            con = 1
            ans.append('NOT BICOLORABLE.')
            break
        else:
            if l[n1]==0 and l[n2]==0:
                l[n1]=1
                l[n2]=2
            elif l[n1]==1:
                l[n2]=2
            elif l[n1]==2:
                l[n2]=1
    if con==0:
        ans.append('BICOLORABLE.')
[print(x)for x in ans]