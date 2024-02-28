l = [0,1]
for i in range(1,5000):
    l.append(l[i]+l[i-1])
ans = []
try:
    while True:
        a = int(input())
        ans.append(f"The Fibonacci number for {a} is {l[a]}")
except EOFError:
    pass
[print(x)for x in ans]