l = [1,2,2]
for i in range(3,77):
    l.append(l[i-3]+l[i-2]) #挑選子集合時一定是從index 1或2
ans = []
try:
    while True:
        a = int(input())
        ans.append(l[a-1])
except EOFError:
    pass
[print(x)for x in ans]