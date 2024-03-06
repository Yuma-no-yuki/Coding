l = [1,1]
for i in range(2,1001):
    l.append(l[i-1]*(i))
ans = []
try:
    while True:
        get = int(input())
        ans.append(f"{get}!")
        ans.append(l[get])
except EOFError:
    pass
[print(x)for x in ans]