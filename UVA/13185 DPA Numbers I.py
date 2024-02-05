ans = []
for x in range(int(input())):
    a = int(input())
    l = []
    for i in range(1,a):
        if a%i == 0:
            l.append(i)
    Sum = sum(l)
    if Sum == a:
        ans.append("perfect")
    elif Sum < a:
        ans.append("deficient")
    else:
        ans.append("abundant")
[print(x)for x in ans]
