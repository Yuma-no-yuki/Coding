dic = {}
for a in range(2,10,2):
    for i in range(10000):
        s = str(i**2)
        s = s.rjust(a,'0')
        s1,s2=s[:len(s)//2],s[len(s)//2:]
        if ((int(s1)+int(s2))**2) == int(s) and len(s) == a:
            dic[s] = a
ans = []
try:
    while True:
        get = int(input())
        for x in dic:
            if dic[x] == get:
                ans.append(x)
except EOFError:
    pass
[print(x)for x in ans]