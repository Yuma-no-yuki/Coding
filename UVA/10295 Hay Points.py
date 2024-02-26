dic = {}
m1,m2 = map(int,input().split(' '))
for i in range(m1):
    n1,n2 = input().split(' ')
    dic[n1] = int(n2)
ans = []
for i in range(m2):
    s = ''
    while True:
        get = input()
        if get=='.':
            break
        s+=get+' '
    add = 0
    for x in s.split(' '):
        if x in dic.keys():
            add += dic[x]
    ans.append(add)
[print(x)for x in ans]