fib = [0,1]
index = 2
for i in range(100):
    if fib[index-1]+fib[index-2] > 100000000:
        break
    fib.append(fib[index-1]+fib[index-2])
    index += 1
fib = fib[2:]
ans = []
for _ in range(int(input())):
    a = int(input())
    or_a = a
    l = []
    while a!=0:
        for x in reversed(fib):
            if x <= a:
                a -= x
                l.append(x)
    s = '0'
    s = s * (fib.index(l[0])+1)
    for x in l:
        s = s[:fib.index(x)]+'1'+s[fib.index(x)+1:]
    ans.append(f"{or_a} = {s[::-1]} (fib)")
[print(x)for x in ans]