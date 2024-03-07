l = [1,2]
for i in range(2,1001):
    l.append(l[i-1]+l[i-2])
ans = []
try:
    while True:
        get = int(input())
        ans.append(l[get])
except EOFError:
    pass
[print(x)for x in ans]