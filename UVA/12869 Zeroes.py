ans = []
while True:
    s = input()
    if s == "0 0":
        break
    a,b = map(int,s.split(' '))
    ans.append(b//5-a//5+1)
[print(x)for x in ans]