ans = []
def gcd(a, b):
    while a != 0:
        b = b % a
        a, b = b, a
    return b
while True:
    get = input()
    if get == '0':
        break
    l=[int(x)for x in get.split(' ')[:-1]]
    Min = min(l)
    l = [int(x)-Min for x in l]
    for x in l:
        if x == 0 :
            l.pop(l.index(x))
    ll = []
    if len(l)==1:
        ans.append(l[0])
    else:
        for i in range(1,len(l)):
            nn = gcd(l[i-1],l[i])
            if nn != 0:
                ll.append(nn)
        ans.append(min(ll))
[print(x)for x in ans]