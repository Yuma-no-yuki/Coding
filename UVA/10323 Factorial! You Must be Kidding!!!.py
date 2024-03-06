l = [1,1]
for i in range(2,16):
    l.append(l[i-1]*(i))
ans = []
try:
    while True:
        get = int(input())
        if get<0 and get%2==1:
            ans.append('Overflow!')
        elif get<0 and get%2==0:
            ans.append('Underflow!')
        elif get>=14:
            ans.append('Overflow!')
        elif get<8:
            ans.append('Underflow!')
        else:
            ans.append(l[get])
except EOFError:
    pass
[print(x)for x in ans]